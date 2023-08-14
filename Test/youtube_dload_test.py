##TEST WILL ASK YOU TO INPUT A YOUTUBE URL, WE SUGGEST A SHORT ONE DUE TO RUNTIM ##
## https://www.youtube.com/watch?v=VsuShNWghXk&ab_channel=wikiHow IS A GOOD URL TO USE## 

import pytest
from app.alpha import API_KEY
from app.youtube_dload import download_and_transcribe

def test_download_and_transcribe(monkeypatch, capsys):
    # Simulate user input for the YouTube URL
    monkeypatch.setattr('builtins.input', lambda _: "https://www.youtube.com/watch?v=VsuShNWghXk&ab_channel=wikiHow")

    # Call the function with the simulated user input
    download_and_transcribe()

    # Capture the printed transcript
    captured = capsys.readouterr()
    transcript = captured.out.strip()

    # Add assertions to validate the transcript
    assert isinstance(transcript, str)
    assert len(transcript) > 0







