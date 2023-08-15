# Youtube-transcript-summarizer

## DESCRIPTION

This app is deisgned to summarize transcripts from a youtube video so a user can save time on watching the video.

It asks a user to input a youtube URL, has a few options for type of summary, then displays the summary text.

It uses pytube to download a youtube video, OpenAI Whisper to transcribe the audio, and then OpenAI ChatCompletion to summarize the text.

*** NOTE ***

You must use a Youtube video less than ~8 minutes long due to size limitations from OpenAI, or else the OpenAI modules will crash.

Example: https://www.youtube.com/watch?v=zBKFt0C3S-0


## Setup

Obtain an [OpenAI API Key]. 

```sh
# this is the ".env" file (in the root directory of the repo)

OPENAI_KEY="____________"
```

Create a virtual environment:

```sh
conda create -n youtube_summarizer-env python=3.10
```

```sh
conda activate youtube_summarizer-env
```

Install third-party packages:

```sh
pip install -r requirements.txt
```

## Usage


Run the app:


```sh
python -m app.youtube_dload
```

## Testing

Run tests:

```sh
pytest
```



# *Not in current version, but future version would include a web app*

Run the web app using the following code: 

## *Mac OS*
FLASK_APP=web_app flask run

## *Windows OS:*
... if `export` doesn't work for you, try `set` instead
... or try a ".env" file approach

export FLASK_APP=web_app
flask run

## *[Deployment Guide](/DEPLOYING.md)*