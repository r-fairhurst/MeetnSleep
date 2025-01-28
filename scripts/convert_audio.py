import subprocess
import os
import sys

def convert_video_to_audio_ffmpeg(video_file, output_ext="wav"):
    """Converts video to audio directly using `ffmpeg` command
    with the help of subprocess module"""

    if not os.path.exists(video_file):
        print(f"Error: File '{video_file}' not found.")
        sys.exit(1)
    filename, ext = os.path.splitext(video_file)
    output_file = f"{filename}.{output_ext}"

    subprocess.call(["ffmpeg", "-y", "-i", video_file, output_file], 
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.STDOUT)
    
    print(f"✔ Successfully converted {video_file} to {output_ext}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Error: No video file provided. Usage: python script.py <video_file>")
        sys.exit(1)
    vf = sys.argv[1]
    
    convert_video_to_audio_ffmpeg(vf)