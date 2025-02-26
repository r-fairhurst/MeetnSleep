import pytest
import os
import sys
import glob

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../main")))
from services.speech_recognition_service import save_transcript

def test_save_invalid_srt(tmp_path):
    """Ensure save_transcript does not create files for invalid SRT data."""
    prefix = "test_transcript"

    # Set storage directory inside the temp path
    storage_dir = tmp_path / "transcripts"
    storage_dir.mkdir(parents=True, exist_ok=True)

    # Test empty transcript
    empty_transcript = []
    save_transcript(empty_transcript, str(storage_dir / prefix))

    # Test incorrectly formatted transcript (missing timestamps)
    invalid_srt = [{"number": 1, "text": "hi there"}]
    save_transcript(invalid_srt, str(storage_dir / prefix))

    # Ensure no files were created
    srt_files = list(storage_dir.glob(f"{prefix}*"))
    assert not srt_files, "Invalid transcript should not be saved, but a file was created."

if __name__ == "__main__":
    test_save_invalid_srt()
    print("✅ Validation test passed!")
