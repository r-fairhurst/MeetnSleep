import os
import sys
import json
from unittest.mock import patch, MagicMock
import main.llms.chatgpt_api 


# Add the parent directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


@patch("main.listen_for_speech")
@patch("main.OpenAI")

def test_main_success(mock_openai, mock_listen_to_speech):
    """ Test successful summary"""
    # mock the envi variable to avoid using real api requests
    os.environ["CHATGPT_API"] = "FAKE_API"

    # simulate user input
    mock_listen_to_speech.return_value = "This is a test to speech summary"

    # mock gpt response