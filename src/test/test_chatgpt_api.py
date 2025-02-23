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
    mock_client = MagicMock()
    mock_openai.return_value = mock_client
    mock_response = MagicMock()
    mock_response.choices = [MagicMock(message=MagicMock(content= "Test summary"))]
    mock_client.chat.completions.create.return_value = mock_response

    # run main 
    with patch("builtins.print") as mock_print:
        main()

    # aseert that the summary was returned
    mock_print.assert_any_call("\nMeeting Summary:")
    mock_print.assert_any_call("Test Summary")


@patch("main.listen_for_speech")
def test_main_success(mock_openai, mock_listen_to_speech):
    """ Test empty string summary"""
    # mock the envi variable to avoid using real api requests
    os.environ["CHATGPT_API"] = "FAKE_API"

    # simulate user empty input
    mock_listen_to_speech.return_value = ""

    with patch("builtins.print") as mock_print:
        main()

    # aseert that the summary was returned empty
    mock_print.assert_any_call("no summary was generated")
    