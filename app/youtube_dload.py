from pytube import YouTube




# Downloading the video
video_url = input("Please input your youtube URL: ")
yt = YouTube(video_url)
stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
stream.download()

# Additional video information
yt = YouTube(video_url)
streams = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc()
top_stream = streams.first()

print("Available streams:")
for stream in streams:
    print(stream)

print("\nTop stream:")
print(top_stream)

# Downloading the top stream
top_stream.download()



from openai import openai

openai.api_key = "sk-..."  # supply your API key however you choose
f = open("path/to/file.mp3", "rb")
transcript = openai.Audio.transcribe("whisper-1", f)




