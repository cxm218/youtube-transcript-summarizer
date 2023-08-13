from flask import Blueprint, request, render_template, redirect, url_for

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
@home_routes.route("/home")
def index():
    print("HOME...")
    return render_template('home.html')
    #return render_template("home.html")

@home_routes.route("/pull_audio", methods=["POST"])
def pull_audio():
    if request.method == "POST":
        video_url = request.form.get("video_url")
        # Download the audio here
        # Redirect to the Summarize page with the video URL as a query parameter
        return redirect(url_for("home_routes.summarize", video_url=video_url))
    
    return render_template('home.html')

@home_routes.route("/summarize")
def summarize():
    print("Summarize Video...")
    video_url = request.args.get("video_url")
    # Perform summarization logic here with the video URL
    summarized_text = "This is a placeholder for the summarized text."

    return render_template("summarize_result.html", summarized_text=summarized_text)

