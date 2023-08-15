#from flask import Blueprint, request, render_template, redirect, url_for
#from pytube import YouTube
#
#home_routes = Blueprint("home_routes", __name__)
#
#@home_routes.route("/")
#@home_routes.route("/home")
#def index():
#    return render_template('home.html')
#
#@home_routes.route("/pull_audio", methods=["POST"])
#def pull_audio():
#    if request.method == "POST":
#        video_url = request.form.get("video_url")
#
#        # Downloading the video using PYTUBE
#        yt = YouTube(video_url)
#        yt.streams.filter(only_audio=True)
#        stream = yt.streams.get_by_itag(22)
#        stream.download()
#
#        # Redirect to the Transcribe page
#        return redirect(url_for("home_routes.transcribe"))
#    
#    return render_template('pull_audio.html')
#
#@home_routes.route("/transcribe")
#def transcribe():
#    return render_template("transcribe.html")
#
#@home_routes.route("/summarize", methods=["GET", "POST"])
#def summarize():
#    if request.method == "POST":
#        # Get the selected summarization option from the form
#        summary_option = request.form.get("summary_option")
#
#        # Perform summarization logic here based on the selected option
#        summarized_text = ""
#
#        if summary_option == "option1":
#            # Perform summarization using option 1
#            summarized_text = "This is a summary generated using option 1."
#
#        elif summary_option == "option2":
#            # Perform summarization using option 2
#            summarized_text = "This is a summary generated using option 2."
#
#        # Add more options and corresponding summarization logic as needed
#
#        return render_template("summarize_result.html", summarized_text=summarized_text)
#
#    return render_template("summarize.html")
