# Sve the Audi to a file 

import requests
import base64
import json

import os
from dotenv import load_dotenv

load_dotenv()

API_BASE_URL = "https://api.sws.speechify.com"
API_KEY = os.getenv('speachifyAPI')
VOICE_ID = "george"

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

def main():
    audio = get_audio("Hello, world!")
    with open("voice/speechify.wav", "wb") as audio_file:
        audio_file.write(audio)   
    # with open("./speech.wav", "wb") as audio_file:
    #     audio_file.write(audio)

if __name__ == "__main__":
    main()
