import os
import sys
import pytest

# Add root MeetnSleep directory
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))) 
#add the src directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

#import the t5 summary module
from main.llms.t5_summary import t_five_summary

#start the pytest
@pytest.fixture
#used for transcript validation
def valid_transcription():
    """Fixture for a valid transcription to be used in the test."""
    return "This is a test transcription. It contains multiple sentences, and we expect it to be summarized."

def test_t_five_summary_with_valid_transcription(valid_transcription):
    
    print("\nUnit test for the t_five_summary function" )

    print("\nCalling the t_five_summary function with a valid transcription...")
    # Step 1: Call the t_five_summary function with the valid transcription. Then retrieve the summary and error from it
    summary, error = t_five_summary(valid_transcription, False)
    
    # Step 2: Check for a thrown error.
    print("Checking for errors...")
    if error: 
        #Add error and signify that the t5 summary has raised an execption
        pytest.fail(f"t5_summary raised an exception: {type(error).__name__}: {error}")
    else:
        print("No error\n")
    # Step 3: Assert that the summary is not empty
    assert summary, "Summary should not be empty."
    
    # Step 4: Assert that the summary is a string
    assert isinstance(summary, str), "Summary should be a string."
    
    # Step 5: check if summary contains relevant content
    assert "test" in summary.lower(), "Summary should contain relevant keywords from the transcription."

#defines the unit test for the t_five summary function from thr t5 api in its use for short transcription
def test_t_five_summary_with_short_transcription():
    """Unit test for the t_five_summary function with a short transcription."""
    
    print("Testing with a short transcription...")
    # A very short transcription
    short_transcription = "Hello world."
    
    # Call the summarization function
    summary, error = t_five_summary(short_transcription, False)

    # Check for a thrown error.
    if error: 
        #return the error and a signify that t5 summary has raised an exception 
        pytest.fail(f"t5_summary raised an exception: {type(error).__name__}: {error}")
    else:
        print("No error\n")
    # Assert that the summary is not empty
    assert summary, "Summary should not be empty."
    
    # Assert that the summary is a string
    assert isinstance(summary, str), "Summary should be a string."
    
    # Check if the summary has meaningful content
    assert "hello" in summary.lower(), "Summary should capture the essence of the short transcription."
