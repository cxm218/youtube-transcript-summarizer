from pytube import YouTube

from openai import openai


# Downloading the video using PYTUBE
video_url = input("Please input your youtube URL: ")
yt = YouTube(video_url)
yt.streams.filter(only_audio=True)
stream = yt.streams.get_by_itag(22)
stream.download()




# create variable for the downloaded file
downloaded_filename = stream.download()



## WHISPER App from Open AI to CREATE TRANSCRIPT

openai.api_key = "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"  # supply your API key however you choose
f = open(downloaded_filename, "rb")
transcript = openai.Audio.transcribe("whisper-1", f)

print(transcript)

