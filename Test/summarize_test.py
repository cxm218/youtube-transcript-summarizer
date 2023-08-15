import pytest
from unittest import mock
from app.youtube_dload import download_and_transcribe, generate_summary

@mock.patch('app.youtube_dload.ChatCompletion.create')
def test_generate_summary(mock_create):
    # Set the mock return value for the summary
    mock_create.return_value.choices[0].message.content = 'Mocked summary text'

    # Call the function with mocked inputs
    chat_text = "Mocked chat text"
    audience = "a programmer"
    summary_length = "1 sentence"
    summary = generate_summary(chat_text, audience, summary_length)

    # Assertion
    assert summary == 'Mocked summary text'

if __name__ == '__main__':
    pytest.main(['-v', '--capture=tee-sys', 'summarize_test.py'])
