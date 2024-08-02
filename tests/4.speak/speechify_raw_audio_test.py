import sounddevice as sd
import numpy as np
import base64
import json
import requests
import os
from pydub import AudioSegment
from io import BytesIO
from dotenv import load_dotenv

load_dotenv()

API_BASE_URL = "https://api.sws.speechify.com"
API_KEY = os.getenv('speachifyAPI')  # Ensure this matches the key in your .env file
VOICE_ID = "Stacy"

def get_audio_data(text):
    url = f"{API_BASE_URL}/v1/audio/speech"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "content-type": "application/json"
    }
    payload = {
        "input": f"<speak>{text}</speak>",
        "voice_id": VOICE_ID,
        "audio_format": "mp3",
    }
    response = requests.post(url, headers=headers, data=json.dumps(payload))

    if response.status_code != 200:
        raise Exception(f"{response.status_code} {response.reason}\n{response.text}")

    response_data = response.json()
    audio_data = base64.b64decode(response_data['audio_data'])

    return audio_data

def play_audio(audio_data):
    # Convert MP3 data to AudioSegment
    audio_segment = AudioSegment.from_file(BytesIO(audio_data), format="mp3")
    
    # Export AudioSegment as raw PCM data
    raw_data = audio_segment.raw_data
    sample_rate = audio_segment.frame_rate
    num_channels = audio_segment.channels
    
    # Convert raw data to numpy array
    audio_array = np.frombuffer(raw_data, dtype=np.int16)
    
    # Play audio using sounddevice
    sd.play(audio_array, samplerate=sample_rate)
    sd.wait()  # Wait until the audio is finished playing

def main():
    text = "say my name say my name"
    audio_data = get_audio_data(text)
    play_audio(audio_data)

if __name__ == "__main__":
    main()
