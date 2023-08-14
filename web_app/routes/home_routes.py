from flask import Blueprint, request, render_template, redirect, url_for
from pytube import YouTube

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
@home_routes.route("/home")
def index():
    return render_template('home.html')

@home_routes.route("/pull_audio", methods=["POST"])
def pull_audio():
    if request.method == "POST":
        video_url = request.form.get("video_url")

        # Downloading the video using PYTUBE
        yt = YouTube(video_url)
        yt.streams.filter(only_audio=True)
        stream = yt.streams.get_by_itag(22)
        stream.download()
        # Redirect to the Summarize page
        return redirect(url_for("home_routes.summarize"))
    
    return render_template('pull_audio.html')

@home_routes.route("/summarize")
def summarize():
    return render_template("summarize_input.html")
