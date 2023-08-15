from pytube import YouTube
import openai
from app.alpha import API_KEY
import os
#from dotenv import load_dotenv

from openai import ChatCompletion

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

    #print(transcript)
    #return transcript

    # OPEN AI SUMMARIZER

    #audience = input('Who is the summary for?')

    chat_text = transcript

    audience = input('Select who the summary is for: \n A) A programmer \n B) A college student \n C) A 2nd grader \n')

    if audience.upper() == 'A':
        audience = "a programmer"
    elif audience.upper() == 'B':
        audience = "a college student"
    elif audience.upper() == 'C':
        audience = "a 2nd grader"
    else:
        print('INVALID RESPONSE. PLEASE TRY AGAIN.')

    #summary_length = input('How long do you want the summary?')
    summary_length = input('Select the type of summary you want: \n A) 1 sentence \n B) 5 bullet points \n C) An outline \n')

    if summary_length.upper() == 'A':
        summary_length = "1 sentence"
    elif summary_length.upper() == 'B':
        summary_length = "5 bullet points"
    elif summary_length.upper() == 'C':
        summary_length = "an outline"
    else:
        print('INVALID RESPONSE. PLEASE TRY AGAIN.')


    chat_completion = ChatCompletion.create(model="gpt-3.5-turbo", messages=[
        {"role": "user", "content": f"Summarize this for {audience} text in {summary_length}: {chat_text}"}
    ])

    # print the chat completion
    print('SUMMARY:')
    print(chat_completion.choices[0].message.content)
    print('END SUMMARY.')




if __name__ == "__main__":
    youtube_url = input("Please input your YouTube URL: ")
    download_and_transcribe(youtube_url)
    

