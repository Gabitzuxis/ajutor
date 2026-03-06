import subprocess

def generate_voice(script, speed):

    with open("script.txt","w") as f:
        f.write(script)

    subprocess.run([
        "espeak",
        "-s",
        str(int(170*speed)),
        "-v",
        "ro",
        "-f",
        "script.txt",
        "-w",
        "voice.wav"
    ])

    return "voice.wav"
