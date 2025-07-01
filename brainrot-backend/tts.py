import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("ELEVENLABS_API_KEY")
if not api_key:
    raise ValueError("ELEVENLABS_API_KEY not found in .env file.")

VOICE_ID = "uju3wxzG5OhpWcoi3SMy"

def generate_tts_audio_and_subs(text: str):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"

    headers = {
        "xi-api-key": api_key,
        "Content-Type": "application/json"
    }

    payload = {
        "text": text,
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {
            "stability": 0.4,
            "similarity_boost": 0.8
        }
    }

    response = requests.post(url, headers=headers, json=payload)
    if response.status_code != 200:
        raise Exception(f"TTS generation failed: {response.status_code} {response.text}")

    os.makedirs("static", exist_ok=True)
    audio_path = "static/audio.mp3"
    with open(audio_path, "wb") as f:
        f.write(response.content)

    subtitle_path = "static/subtitles.json"

    grouped_subs = []
    group_size = 5  # 4 or 5 is a good value
    words = text.strip().split()
    time_per_word = 0.35

    for i in range(0, len(words), group_size):
        chunk = words[i:i+group_size]
        phrase = " ".join(chunk)
        start = i * time_per_word
        end = start + (len(chunk) * time_per_word)
        grouped_subs.append({"start": start, "end": end, "text": phrase})

    with open(subtitle_path, "w") as f:
        json.dump(grouped_subs, f)

    return audio_path, subtitle_path
