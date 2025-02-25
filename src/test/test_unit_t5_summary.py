import os
import sys
import pytest

# Add both the root 'MeetnSleep' directory and 'src' directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))  # Root directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..", "src")))  # src directory

from main.llms.t5_summary import t_five_summary

@pytest.fixture
def valid_transcription():
    """Fixture for a valid transcription to be used in the test."""
    return "This is a test transcription. It contains multiple sentences, and we expect it to be summarized."

def test_t_five_summary_with_valid_transcription(valid_transcription):
    """Unit test for the t_five_summary function."""
    
    # Step 1: Call the t_five_summary function with the valid transcription.
    summary = t_five_summary(valid_transcription, False)
    
    # Step 2: Assert that the summary is not empty
    assert summary, "Summary should not be empty."
    
    # Step 3: Assert that the summary is a string
    assert isinstance(summary, str), "Summary should be a string."
    
    # Step 4: (Optional) You can also check if the summary contains relevant content
    assert "test" in summary.lower(), "Summary should contain relevant keywords from the transcription."

def test_t_five_summary_with_short_transcription():
    """Unit test for the t_five_summary function with a short transcription."""
    
    # A very short transcription
    short_transcription = "Hello world."
    
    # Call the summarization function
    summary = t_five_summary(short_transcription, False)
    
    # Assert that the summary is not empty
    assert summary, "Summary should not be empty."
    
    # Assert that the summary is a string
    assert isinstance(summary, str), "Summary should be a string."
    
    # Check if the summary has meaningful content
    assert "hello" in summary.lower(), "Summary should capture the essence of the short transcription."
