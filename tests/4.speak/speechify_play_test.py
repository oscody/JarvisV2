import requests
import base64
import json
import simpleaudio as sa

import os
from dotenv import load_dotenv

load_dotenv()

API_BASE_URL = "https://api.sws.speechify.com"
API_KEY = os.getenv('speachifyAPI')
VOICE_ID = "Stacy"

def get_audio(text):
    url = f"{API_BASE_URL}/v1/audio/speech"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "content-type": "application/json"
    }
    payload = {
        "input": f"<speak>{text}</speak>",
        "voice_id": VOICE_ID,
        "audio_format": "wav",
    }
    response = requests.post(url, headers=headers, data=json.dumps(payload))

    if response.status_code != 200:
        raise Exception(f"{response.status_code} {response.reason}\n{response.text}")

    response_data = response.json()
    audio_data = base64.b64decode(response_data['audio_data'])

    return audio_data

def play_audio(audio_data):
    # Write the audio data to a temporary file
    with open("Voice/speechify_speech.wav", "wb") as audio_file:
        audio_file.write(audio_data)
    
    # Play the audio
    wave_obj = sa.WaveObject.from_wave_file("Voice/speechify_speech.wav")
    play_obj = wave_obj.play()
    play_obj.wait_done()

def main():
    audio = get_audio("say my name say my name say my name ")
    play_audio(audio)

if __name__ == "__main__":
    main()
