import subprocess
import json

from backend.voice_engine import generate_voice
from backend.image_engine import generate_images

def get_audio_duration(file):

    result = subprocess.run(
        [
            "ffprobe",
            "-v","error",
            "-show_entries","format=duration",
            "-of","json",
            file
        ],
        capture_output=True,
        text=True
    )

    data = json.loads(result.stdout)

    return float(data["format"]["duration"])


def generate_video(script, prompts, speed):

    voice = generate_voice(script, speed)

    images = generate_images(prompts)

    audio_duration = get_audio_duration(voice)

    duration = audio_duration / len(images)

    inputs=[]

    for img in images:
        inputs += ["-loop","1","-t",str(duration),"-i",img]

    cmd=[
        "ffmpeg",
        *inputs,
        "-i",voice,
        "-pix_fmt","yuv420p",
        "-shortest",
        "output.mp4"
    ]

    subprocess.run(cmd)

    return "output.mp4"
