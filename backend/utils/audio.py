import subprocess,json

def get_audio_duration(file):

    r=subprocess.run(
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

    data=json.loads(r.stdout)

    return float(data["format"]["duration"])
