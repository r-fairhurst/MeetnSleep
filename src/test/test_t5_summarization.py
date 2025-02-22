import os
import sys
import json
import pytest
from tqdm import tqdm

# Add the parent directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from main.llms.t5_summary import t_five_summary

# RUN WITH pytest OR pytest -s

@pytest.fixture(scope="module")
def transcript_files():
    """Get the transcript names from the JSON file."""
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    inputs_path = os.path.join(base_dir, "test", "test_summarization_inputs", "test_inputs.json")
    with open(inputs_path, "r", encoding="utf-8") as f:
        return json.load(f)

def test_t5_summary(transcript_files):
    """Test T5 summary on multiple transcript files with progress bar."""
    
    # This line shows which file is being tested currently
    tqdm.write("\n")
    
    total_tests = len(transcript_files)
    assert total_tests > 0, "No test files found in the JSON list."

    # Iterate with tqdm loading bar
    for file_name in tqdm(transcript_files, desc="Testing Summaries", ncols=75):
        base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        file_path = os.path.join(base_dir, "test", "test_summarization_inputs", file_name)
        assert os.path.exists(file_path), f"Transcript file {file_name} does not exist."

        with open(file_path, "r", encoding="utf-8") as file:
            transcript_content = file.read()

        try:
            summary = t_five_summary(transcript_content, False)
            # If the file has content, summary shouldn't be None
            if transcript_content.strip():
                assert summary is not None, f"Summary is None for {file_name}"
        except Exception as e:
            pytest.fail(f"t_five_summary raised an exception for {file_name}: {e}")

        tqdm.write(f"{file_name}: Summary returned")
