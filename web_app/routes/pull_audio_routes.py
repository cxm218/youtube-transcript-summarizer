# this is the "web_app/routes/pull_audio_routes.py" file ...

import os
from flask import Blueprint, request, render_template, redirect, flash
from pytube import YouTube
import openai
from dotenv import load_dotenv  # Import the dotenv module

pull_audio_routes = Blueprint("pull_audio_routes", __name__)

# Load the environment variables from the .env file
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
        api_key = os.getenv("OPENAI_API_KEY")  # Retrieve the API key from the environment variable
        openai.api_key = api_key
        f = open(downloaded_filename, "rb")
        transcript = openai.Audio.transcribe("whisper-1", f)

        return render_template("audio_result.html", transcript=transcript)

    return render_template("audio_input.html")

