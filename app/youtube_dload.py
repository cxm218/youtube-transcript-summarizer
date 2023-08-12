from pytube import YouTube

import openai

from app.alpha import API_KEY


# Downloading the video using PYTUBE
video_url = input("Please input your youtube URL: ")
yt = YouTube(video_url)
yt.streams.filter(only_audio=True)
stream = yt.streams.get_by_itag(22)
stream.download()




# create variable for the downloaded file
downloaded_filename = stream.download()



## WHISPER App from Open AI to CREATE TRANSCRIPT

openai.api_key = API_KEY  # supply your API key however you choose
f = open(downloaded_filename, "rb")
transcript = openai.Audio.transcribe("whisper-1", f)

print(transcript)

