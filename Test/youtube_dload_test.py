import pytest
from app.alpha import API_KEY
from app.youtube_dload import download_and_transcribe

def test_download_and_transcribe(monkeypatch):
    # Simulate user input for the YouTube URL
    monkeypatch.setattr('builtins.input', lambda _: "https://www.youtube.com/watch?v=VsuShNWghXk&ab_channel=wikiHow")

    transcript = download_and_transcribe()

    assert isinstance(transcript, str)
    assert len(transcript) > 0






