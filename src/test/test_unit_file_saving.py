import os
import pytest
import glob
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../main")))
from services.speech_recognition_service import save_transcript

def test_save_srt_transcript(tmp_path):
    prefix = "test_transcript"
    transcript = [
        {
            "number": 1,
            "start_time": "00:00:00,000",
            "end_time": "00:00:04,969",
            "text": "hi there"
        }
    ]

    # Using a temp directory
    storage_dir = tmp_path / "transcripts"
    storage_dir.mkdir(parents=True, exist_ok=True)

    try:
        # Attempt to save the transcript
        save_transcript(transcript, str(storage_dir / prefix))
    except OSError as e:
        if str(e) == "No Default Input Device Available":
            pytest.skip("No default input device available, skipping test.")
        else:
            raise  # Re-raise the error if it's something else
    # Find the file that matches our prefix
    matching_files = list(storage_dir.glob(f"{prefix}*.srt"))
    assert matching_files, "No transcript file with the expected prefix was found."

    file_path = matching_files[0]  # Take the first matching file
    try:
        with open(file_path, "r") as f:
            expected_content = """1
00:00:00,000 --> 00:00:04,969
hi there
"""
            assert f.read().strip() == expected_content.strip(), "Stored transcript does not match expected content."
    finally:
        file_path.unlink()  # Cleanup safely

