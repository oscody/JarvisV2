import os
import time
import uuid
import numpy as np
from dotenv import load_dotenv
from elevenlabs import VoiceSettings
from elevenlabs.client import ElevenLabs
from pydub import AudioSegment
import simpleaudio as sa
import requests
import base64
import json
import sounddevice as sd
from piper.voice import PiperVoice

# Load environment variables
load_dotenv()

# API keys and configuration
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
SPEECHIFY_API_KEY = os.getenv('speachifyAPI')
PIPER_VOICEDIR = "pipertts/"
PIPER_MODEL = PIPER_VOICEDIR + "en_US-norman-medium.onnx"
PIPER_CONFIG = PIPER_VOICEDIR + "en_en_US_norman_medium_en_US-norman-medium.onnx.json"

if not ELEVENLABS_API_KEY:
    raise ValueError("ELEVENLABS_API_KEY environment variable not set")
if not SPEECHIFY_API_KEY:
    raise ValueError("SPEACHIFY_API environment variable not set")

# ElevenLabs client
elevenlabs_client = ElevenLabs(api_key=ELEVENLABS_API_KEY)

# Functions to generate and play TTS audio using different APIs

# ElevenLabs
def elevenlabs_text_to_speech(text: str) -> str:
    try:
        response = elevenlabs_client.text_to_speech.convert(
            voice_id="N2lVS1w4EtoT3dr4eOWO",
            optimize_streaming_latency="0",
            output_format="mp3_22050_32",
            text=text,
            model_id="eleven_turbo_v2",
            voice_settings=VoiceSettings(
                stability=0.0,
                similarity_boost=1.0,
                style=0.0,
                use_speaker_boost=True,
            ),
        )
        mp3_file_path = f"Voice/elevenlabs_speech.mp3"
        wav_file_path = f"Voice/elevenlabs_speech.wav"
        with open(mp3_file_path, "wb") as f:
            for chunk in response:
                if chunk:
                    f.write(chunk)
        sound = AudioSegment.from_mp3(mp3_file_path)
        sound.export(wav_file_path, format="wav")
        return wav_file_path
    except Exception as e:
        print(f"Error generating ElevenLabs audio: {e}")
        return None

# Speechify
def speechify_text_to_speech(text: str) -> str:
    try:
        url = f"https://api.sws.speechify.com/v1/audio/speech"
        headers = {
            "Authorization": f"Bearer {SPEECHIFY_API_KEY}",
            "content-type": "application/json"
        }
        payload = {
            "input": f"<speak>{text}</speak>",
            "voice_id": "Stacy",
            "audio_format": "wav",
        }
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        if response.status_code != 200:
            raise Exception(f"{response.status_code} {response.reason}\n{response.text}")
        response_data = response.json()
        audio_data = base64.b64decode(response_data['audio_data'])
        wav_file_path = "Voice/speechify_speech.wav"
        with open(wav_file_path, "wb") as f:
            f.write(audio_data)
        return wav_file_path
    except Exception as e:
        print(f"Error generating Speechify audio: {e}")
        return None


    try:
        voice = PiperVoice.load(PIPER_MODEL, PIPER_CONFIG)
        wav_file_path = "Voice/piper_speech.wav"
        with sd.OutputStream(samplerate=voice.config.sample_rate, channels=1, dtype='int16') as stream:
            for audio_bytes in voice.synthesize_stream_raw(text):
                int_data = np.frombuffer(audio_bytes, dtype=np.int16)
                stream.write(int_data)
        return wav_file_path
    except Exception as e:
        print(f"Error generating Piper audio: {e}")
        return None

# Function to play audio using simpleaudio
def play_audio(file_path: str):
    if file_path and os.path.exists(file_path):
        wave_obj = sa.WaveObject.from_wave_file(file_path)
        play_obj = wave_obj.play()
        play_obj.wait_done()
    else:
        print(f"File not found: {file_path}")

# Main test function
def test_playback_speed():
    text = "Hello, this is a test of the text-to-speech system."

    # ElevenLabs Test
    elevenlabs_wav = elevenlabs_text_to_speech(text)
    start_time = time.time()
    play_audio(elevenlabs_wav)
    elevenlabs_playback_time = time.time() - start_time

    # Speechify Test
    speechify_wav = speechify_text_to_speech(text)
    start_time = time.time()
    play_audio(speechify_wav)
    speechify_playback_time = time.time() - start_time

    # # Piper Test
    piper_wav = piper_text_to_speech(text)
    start_time = time.time()
    play_audio(piper_wav)
    piper_playback_time = time.time() - start_time

    # Print results
    print(f"ElevenLabs playback time: {elevenlabs_playback_time:.4f} seconds")
    print(f"Speechify playback time: {speechify_playback_time:.4f} seconds")
    print(f"Piper playback time: {piper_playback_time:.4f} seconds")

if __name__ == "__main__":
    test_playback_speed()
