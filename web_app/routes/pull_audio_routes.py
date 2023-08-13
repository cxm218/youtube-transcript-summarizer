import os
from flask import Blueprint, request, render_template, redirect, flash, url_for
from pytube import YouTube
import openai
from dotenv import load_dotenv

pull_audio_routes = Blueprint("pull_audio_routes", __name__)

load_dotenv()

@pull_audio_routes.route("/pull-audio", methods=["GET", "POST"])
def pull_audio():
    if request.method == "POST":
        video_url = request.form.get("video_url")

        # Downloading the video using PYTUBE
        yt = YouTube(video_url)
        yt.streams.filter(only_audio=True)
        stream = yt.streams.get_by_itag(22)
        stream.download()
        downloaded_filename = stream.download()

        # WHISPER App from Open AI to CREATE TRANSCRIPT
        api_key = os.getenv("OPENAI_API_KEY")
        openai.api_key = api_key
        f = open(downloaded_filename, "rb")
        transcript = openai.Audio.transcribe("whisper-1", f)

        # Redirect to the Summarize Video page with the transcript as a query parameter
        return redirect(url_for("pull_audio_routes.summarize_video", transcript=transcript))

    return render_template("audio_input.html")

@pull_audio_routes.route("/summarize-video", methods=["GET", "POST"])
def summarize_video():
    if request.method == "POST":
        # Perform summarization logic here using the selected option
        summary_option = request.form.get("summary_option")
        summarized_text = "This is a placeholder for the summarized text based on the selected option."

        return render_template("summarize_video.html", summarized_text=summarized_text)

    # Redirect back to the Pull Audio page if accessed directly
    return redirect(url_for("pull_audio_routes.pull_audio"))


