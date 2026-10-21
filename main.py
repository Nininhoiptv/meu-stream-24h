import os
import subprocess

STREAM_KEY = os.environ.get("STREAM_KEY")
STREAM_URL = f"rtmp://a.rtmp.youtube.com/live2/{STREAM_KEY}"

cmd = [
    "ffmpeg",
    "-re",
    "-stream_loop", "-1",
    "-i", "video.mp4",
    "-c:v", "libx264",
    "-preset", "veryfast",
    "-maxrate", "2500k",
    "-bufsize", "5000k",
    "-pix_fmt", "yuv420p",
    "-g", "50",
    "-c:a", "aac",
    "-b:a", "128k",
    "-ar", "44100",
    "-f", "flv",
    STREAM_URL
]

subprocess.run(cmd)
