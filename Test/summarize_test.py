import pytest
from unittest import mock
from app.summarize import get_audience, get_summary_length, generate_summary

def test_get_audience(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'A')
    audience = get_audience()
    assert audience == 'a programmer'

def test_get_summary_length(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 'B')
    summary_length = get_summary_length()
    assert summary_length == '5 bullet points'

@mock.patch('app.summarize.ChatCompletion.create')
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
