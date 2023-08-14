
# this is the "test/youtube_dloat_test.py" file...

from audio_transcription import download_and_transcribe

def test_download_and_transcribe():
    # Replace with an actual YouTube URL for testing
    youtube_url = "https://www.youtube.com/watch?v=p0Eue_hmJ28&ab_channel=AlBrady"
    transcript = download_and_transcribe(youtube_url)

    # Add assertions to validate the transcription
    assert isinstance(transcript, str)
    assert len(transcript) > 0
