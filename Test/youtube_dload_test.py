import pytest
from app.alpha import API_KEY
from app.youtube_dload import download_and_transcribe
from unittest import mock

def test_download_and_transcribe(monkeypatch, capsys):
    # Mock the API_KEY and API request to avoid actual API calls
    with mock.patch('app.youtube_dload.API_KEY', 'abc123'), \
         mock.patch('openai.Audio.transcribe') as mock_transcribe:

        # Set the mock return value for the transcript
        mock_transcribe.return_value = "Mocked transcript text"

        # Simulate user input for the YouTube URL
        monkeypatch.setattr('builtins.input', lambda _: "https://www.youtube.com/watch?v=VsuShNWghXk&ab_channel=wikiHow")

        # Call the function with the simulated user input
        transcript = download_and_transcribe()
        assert isinstance(transcript, str)
        assert len(transcript) > 0
