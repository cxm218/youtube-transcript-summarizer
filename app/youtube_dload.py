from pytube import YouTube
import openai
from app.alpha import API_KEY

def download_and_transcribe(video_url=None):
    if video_url is None:
        video_url = input("Please input your YouTube URL: ")

    # Downloading the video using PYTUBE
    yt = YouTube(video_url)
    yt.streams.filter(only_audio=True)
    stream = yt.streams.get_by_itag(22)
    stream.download()

    # create variable for the downloaded file
    downloaded_filename = stream.download()

    # WHISPER App from Open AI to CREATE TRANSCRIPT
    openai.api_key = API_KEY
    f = open(downloaded_filename, "rb")
    transcript = openai.Audio.transcribe("whisper-1", f)

    print(transcript)

if __name__ == "__main__":
    youtube_url = input("Please input your YouTube URL: ")
    download_and_transcribe(youtube_url)


