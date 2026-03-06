import subprocess

from backend.voice_engine import generate_voice
from backend.image_engine import generate_images
from backend.utils.audio import get_audio_duration

def generate_video(script,prompts,speed):

    voice=generate_voice(script,speed)

    images=generate_images(prompts)

    audio_duration=get_audio_duration(voice)

    duration=audio_duration/len(images)

    inputs=[]

    for img in images:

        inputs += [
            "-loop","1",
            "-t",str(duration),
            "-i",img
        ]

    cmd=[
        "ffmpeg",
        *inputs,
        "-i",voice,
        "-vf",
        "scale=1080:1920,zoompan=z='zoom+0.0005':d=125",
        "-pix_fmt","yuv420p",
        "-shortest",
        "output.mp4"
    ]

    subprocess.run(cmd)

    return "output.mp4"
