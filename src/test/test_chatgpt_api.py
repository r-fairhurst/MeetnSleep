# src/test/test_chatgpt_api.py
import os
import sys
from unittest.mock import patch, MagicMock
from main.llms.chatgpt_api import main, setup_openai_client, openai_summary

@patch("main.llms.chatgpt_api.listen_for_speech")
@patch("main.llms.chatgpt_api.OpenAI")

def test_openai_summary_success(mock_openai, mock_listen):
    """Test successful summary generation with OpenAI API and speech input"""
    os.environ["CHATGPT_API"] = "FAKE_OPENAI_KEY"
    mock_listen.return_value = "This is a test transcript"
    mock_client = MagicMock()
    mock_openai.return_value = mock_client
    mock_response = MagicMock()
    mock_response.choices = [MagicMock(message=MagicMock(content="Summary of the meeting"))]
    mock_client.chat.completions.create.return_value = mock_response

    with patch("builtins.print") as mock_print:
        summary, error = openai_summary(True)
    
    assert summary == "Summary of the meeting"
    assert error is None
    mock_print.assert_any_call("\nOpenAI Meeting Summary:\n")
    mock_print.assert_any_call("Summary of the meeting")
    

@patch("main.llms.chatgpt_api.listen_for_speech")
@patch("main.llms.chatgpt_api.OpenAI")
def test_openai_summary_error(mock_openai, mock_listen):
    """Test error handling when OpenAI API fails"""
    os.environ["CHATGPT_API"] = "FAKE_OPENAI_KEY"
    mock_listen.return_value = "This is a test transcript"
    mock_client = MagicMock()
    mock_openai.return_value = mock_client
    mock_client.chat.completions.create.side_effect = Exception("API Failure")

    with patch("builtins.print") as mock_print:
        summary, error = openai_summary(False)
    
    assert summary is None
    assert isinstance(error, Exception)
    assert str(error) == "API Failure"
    mock_print.assert_any_call("OpenAI API Error: API Failure")

@patch("main.llms.chatgpt_api.listen_for_speech")
def test_openai_summary_missing_key(mock_listen):
    """Test behavior when CHATGPT_API key is missing"""
    if "CHATGPT_API" in os.environ:
        del os.environ["CHATGPT_API"]
    mock_listen.return_value = "This is a test transcript"

    with patch("builtins.print") as mock_print:
        summary, error = openai_summary(False)
    
    assert summary is None
    assert error is None
    mock_print.assert_any_call("OpenAI API key not found. Please set it as an environment variable.")


@patch("main.llms.chatgpt_api.listen_for_speech")
@patch("main.llms.chatgpt_api.OpenAI")
def test_openai_summary_no_speech(mock_openai, mock_listen):
    """Test behavior when no speech is captured"""
    os.environ["CHATGPT_API"] = "FAKE_OPENAI_KEY"
    mock_listen.return_value = None

    with patch("builtins.print") as mock_print:
        summary, error = openai_summary(False)
    
    assert summary is None
    assert error is None
    mock_print.assert_any_call("No transcript generated. Exiting...")

if __name__ == "__main__":
    import pytest
    pytest.openai_summary([__file__])