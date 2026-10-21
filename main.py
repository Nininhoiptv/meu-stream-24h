import os
import subprocess

# Pega o link RTMP do SSH101 direto do Render
STREAM_URL = os.environ.get("STREAM_URL")

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

subprocess.run(cmd)a
