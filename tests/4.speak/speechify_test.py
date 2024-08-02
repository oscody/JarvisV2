# # Sve the Audi to a file 

# import requests
# import base64
# import json

# import os
# from dotenv import load_dotenv

# load_dotenv()

# API_BASE_URL = "https://api.sws.speechify.com"
# API_KEY = os.getenv('speachifyAPI')
# VOICE_ID = "george"

# def get_audio(text):
#     url = f"{API_BASE_URL}/v1/audio/speech"
#     headers = {
#         "Authorization": f"Bearer {API_KEY}",
#         "content-type": "application/json"
#     }
#     payload = {
#         "input": f"<speak>{text}</speak>",
#         "voice_id": VOICE_ID,
#         "audio_format": "wav",
#     }
#     response = requests.post(url, headers=headers, data=json.dumps(payload))

#     if response.status_code != 200:
#         raise Exception(f"{response.status_code} {response.reason}\n{response.text}")

#     response_data = response.json()
#     audio_data = base64.b64decode(response_data['audio_data'])

#     return audio_data

# def main():
#     audio = get_audio("Hello, world!")
#     with open("Voice/speechify.wav", "wb") as audio_file:
#         audio_file.write(audio)   
#     # with open("./speech.wav", "wb") as audio_file:
#     #     audio_file.write(audio)

# if __name__ == "__main__":
#     main()




import time
import sounddevice as sd
import numpy as np
import base64
import json
import requests
import os
from pydub import AudioSegment
from io import BytesIO
from dotenv import load_dotenv
import simpleaudio as sa

load_dotenv()

API_BASE_URL = "https://api.sws.speechify.com"
API_KEY = os.getenv('speachifyAPI')
VOICE_ID = "Stacy"

def get_audio_data(text, format="mp3"):
    url = f"{API_BASE_URL}/v1/audio/speech"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "content-type": "application/json"
    }
    payload = {
        "input": f"<speak>{text}</speak>",
        "voice_id": VOICE_ID,
        "audio_format": format,
    }
    response = requests.post(url, headers=headers, data=json.dumps(payload))

    if response.status_code != 200:
        raise Exception(f"{response.status_code} {response.reason}\n{response.text}")

    response_data = response.json()
    audio_data = base64.b64decode(response_data['audio_data'])

    return audio_data

def play_audio_raw(audio_data):
    audio_segment = AudioSegment.from_file(BytesIO(audio_data), format="mp3")
    raw_data = audio_segment.raw_data
    sample_rate = audio_segment.frame_rate
    
    audio_array = np.frombuffer(raw_data, dtype=np.int16)
    sd.play(audio_array, samplerate=sample_rate)
    sd.wait()

def play_audio_file(audio_data):
    with open("Voice/speechify_speech.wav", "wb") as audio_file:
        audio_file.write(audio_data)
    
    wave_obj = sa.WaveObject.from_wave_file("Voice/speechify_speech.wav")
    play_obj = wave_obj.play()
    play_obj.wait_done()

def main():
    text = "If no one is around you Say baby I love you If you ain't runnin' game"
    # Test raw audio playback
    audio_data_mp3 = get_audio_data(text, format="mp3")
    
    start_time = time.time()
    play_audio_raw(audio_data_mp3)
    raw_playback_time = time.time() - start_time
    
    print(f"Time taken to play raw audio: {raw_playback_time:.2f} seconds")

    # Test file playback
    audio_data_wav = get_audio_data(text, format="wav")
    
    start_time = time.time()
    play_audio_file(audio_data_wav)
    file_playback_time = time.time() - start_time
    
    print(f"Time taken to play audio from file: {file_playback_time:.2f} seconds")

if __name__ == "__main__":
    main()
