import pytest
import os
import sys
import glob

# Append the path to import your modules correctly
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../main")))
from services.speech_recognition_service import save_transcript

@pytest.fixture
def edge_case_transcript():
    """Simulate transcript with edge cases"""
    return [
        {
            'number': 1,
            'start_time': '00:00:00,000',
            'end_time': '00:00:10,000',
            'text': 'A' * 10000  # Very long text
        },
        {
            'number': 2,
            'start_time': '00:00:10,000',
            'end_time': '00:00:20,000',
            'text': ''  # Empty text
        }
    ]

def test_save_edge_case_transcripts(edge_case_transcript, tmp_path):
    """Test saving transcript with edge case content (long and empty text)."""
    # Temporary directory for the transcript
    storage_dir = tmp_path / "transcripts"
    storage_dir.mkdir(parents=True, exist_ok=True)
    
    # Save the transcript
    save_transcript(edge_case_transcript, file_prefix="edge_case_test")
    
    # Find the file that matches the prefix using glob
    file_pattern = str(storage_dir / "edge_case_test*.srt")
    matching_files = glob.glob(file_pattern)
    
    print(f"Matching files: {matching_files}")  # Debug print
    
    # Ensure the file was created
    assert matching_files, "No transcript file found."
    
    file_path = matching_files[0]  # Get the first matching file
    
    # Read and verify file content
    with open(file_path, "r", encoding="utf-8") as file:
        file_content = file.read().strip()
    
    expected_content = "\n".join([
        f"1\n00:00:00,000 --> 00:00:10,000\n{'A' * 10000}\n",
        "2\n00:00:10,000 --> 00:00:20,000\n\n"
    ]).strip()
    
    assert file_content == expected_content, f"Expected: {expected_content}\nActual: {file_content}"
