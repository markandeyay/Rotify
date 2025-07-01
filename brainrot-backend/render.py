import os
import subprocess
import uuid

FFMPEG_PATH = r"C:\\Users\\yalam\\Downloads\\ffmpeg\\bin\\ffmpeg.exe" # Replace with your path :-)
BASE_VIDEO_PATH = os.path.join("static", "subway.mp4")

def generate_video(summary: str, audio_path: str) -> str:
    if not os.path.exists(BASE_VIDEO_PATH):
        raise FileNotFoundError("subway.mp4 not found in static/. Place it there.")

    if not os.path.exists(audio_path):
        raise FileNotFoundError(f"Missing {audio_path}. Place it in the correct directory.")

    # Generate random unique filename for vid
    video_filename = f"{uuid.uuid4()}_final.mp4"
    output_path = os.path.join("static", video_filename)

    cmd = [
        FFMPEG_PATH,
        "-y",  # overwrite
        "-i", BASE_VIDEO_PATH,
        "-i", audio_path,
        "-c:v", "copy",
        "-c:a", "aac",
        "-shortest",
        output_path
    ]

    subprocess.run(cmd, check=True)

    return output_path
