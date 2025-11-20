import tempfile
import time
from pathlib import Path
from google.generativeai import upload_file, get_file


def save_temp_video(video_file):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp_video:
        temp_video.write(video_file.read())
        return temp_video.name


def process_video(video_path):
    processed_video = upload_file(video_path)
    while processed_video.state.name == "PROCESSING":
        time.sleep(1)
        processed_video = get_file(processed_video.name)
    return processed_video


def cleanup_temp_file(file_path):
    Path(file_path).unlink(missing_ok=True)
