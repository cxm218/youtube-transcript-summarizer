# Unemployment-in-class-project

## Setup

Obtain an [OpenAI API Key]. 

```sh
# this is the ".env" file (in the root directory of the repo)

OPENAI_KEY="____________"

Create a virtual environment:

```sh
conda create -n unemployment-env python=3.10
```

```sh
conda activate unemployment-env
```

Install third-party packages:

```sh
pip install -r requirements.txt
```

## Usage

Pull the Audio:

```sh
python app/pull-audio.py

python -m app.pull-audio

```
Run the web app using the following code: 

# Mac OS
FLASK_APP=web_app flask run

# Windows OS:
# ... if `export` doesn't work for you, try `set` instead
# ... or try a ".env" file approach
export FLASK_APP=web_app
flask run
## Testing

Run tests:

```sh
pytest
```
## [Deployment Guide](/DEPLOYING.md)