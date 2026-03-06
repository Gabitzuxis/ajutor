import subprocess

def generate_voice(script,speed):

    with open("script.txt","w") as f:
        f.write(script)

    rate = int(170*float(speed))

    subprocess.run([
        "espeak",
        "-v","ro",
        "-s",str(rate),
        "-f","script.txt",
        "-w","voice.wav"
    ])

    return "voice.wav"
