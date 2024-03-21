import os
import base64
from elevenlabs import generate, play

def play_audio(text):
    audio = generate(text, voice='Bv9wCJUMqXd6UOxI1UVr')

    unique_id = base64.urlsafe_b64encode(os.urandom(30)).decode("utf-8").rstrip("=")
    dir_path = os.path.join("records", unique_id)
    os.makedirs(dir_path, exist_ok=True)
    file_path = os.path.join(dir_path, "audio.wav")

    with open(file_path, "wb") as f:
        f.write(audio)

    play(audio)