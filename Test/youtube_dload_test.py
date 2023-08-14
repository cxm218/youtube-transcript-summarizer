

import pytest
from app.alpha import API_KEY
from app.youtube_dload import download_and_transcribe
from unittest import mock

def test_download_and_transcribe(monkeypatch, capsys):
    # Mock the API_KEY and API request to avoid actual API calls
    with mock.patch('app.alpha.API_KEY', 'your_mocked_api_key'), \
         mock.patch('openai.Audio.transcribe') as mock_transcribe:

        # Set the mock return value for the transcript
        mock_transcribe.return_value = "Mocked transcript text"

        # Simulate user input for the YouTube URL
        monkeypatch.setattr('builtins.input', lambda _: "https://www.youtube.com/watch?v=VsuShNWghXk&ab_channel=wikiHow")

        # Call the function with the simulated user input
        download_and_transcribe()

        # Capture the printed transcript
        captured = capsys.readouterr()
        transcript = captured.out.strip()

        # Assertions
        assert isinstance(transcript, str)
        assert len(transcript) > 0









