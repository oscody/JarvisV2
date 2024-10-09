

import soundfile as sf

import sounddevice as sd
import numpy as np

import base64
import json
import requests
import os
from pydub import AudioSegment
from io import BytesIO
from dotenv import load_dotenv

from elevenlabs import VoiceSettings
from elevenlabs.client import ElevenLabs
from playsound import playsound
import pygame

ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
elevenLabs_bogle_voiceID = os.getenv("elevenLabs_bogle_voiceID")

if not ELEVENLABS_API_KEY:
    raise ValueError("ELEVENLABS_API_KEY environment variable not set")

client = ElevenLabs(
    api_key=ELEVENLABS_API_KEY,
)

audioPath = "Voice/Wolf.wav"


load_dotenv()

API_BASE_URL = "https://api.sws.speechify.com"
API_KEY = os.getenv('speachifyAPI')  # Ensure this matches the key in your .env file
VOICE_ID = "Stacy"

def geneate_audio_tts(text_to_speak):

    import torch
    from TTS.tts.configs.xtts_config import XttsConfig
    from TTS.tts.models.xtts import Xtts

    print("geneate_audio...")

    config = XttsConfig()
    config.load_json("./XTTS-v2/config.json")
    model = Xtts.init_from_config(config)
    model.load_checkpoint(config, checkpoint_dir="./XTTS-v2/")

    # Check if CUDA is available and move the model to the appropriate device
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)



    # Use XTTS to synthesize speech
    outputs = model.synthesize(
        text_to_speak,  # Pass the prompt as a string directly
        config,
        speaker_wav=audioPath,  # Pass the file path directly
        gpt_cond_len=24,
        temperature=0.5,
        language='en',
        speed=1.4  # Specify the desired language
    )

    #Get the synthesized audio tensor from the dictionary
    synthesized_audio = outputs['wav']


    output_file_path = './outputs/output_audio.wav'
    sample_rate = config.audio.sample_rate
    sf.write(output_file_path, synthesized_audio, sample_rate)
    return output_file_path


def geneate_ppt_audio(text_to_speak):

    from piper.voice import PiperVoice

    print("Playing...audio")

    voicedir = "pipertts/" # Where onnx model files are stored on my machine
    model = voicedir + "en_US-norman-medium.onnx"
    config = voicedir + "en_en_US_norman_medium_en_US-norman-medium.onnx.json" # Correct config file name

    # Load the model and config
    voice = PiperVoice.load(model, config)

    # Setup a sounddevice OutputStream with appropriate parameters
    # The sample rate and channels should match the properties of the PCM data
    stream = sd.OutputStream(samplerate=voice.config.sample_rate, channels=1, dtype='int16')
    stream.start()

    for audio_bytes in voice.synthesize_stream_raw(text_to_speak):
        int_data = np.frombuffer(audio_bytes, dtype=np.int16)
        stream.write(int_data)
    

    print("stoping...audio")

    stream.stop()
    stream.close()
    


def geneate_speechify_audio(text):

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





def generate_elevenlabs_audio(text: str) -> str:

    # Calling the text_to_speech conversion API with detailed parameters
    response = client.text_to_speech.convert(
        voice_id=elevenLabs_bogle_voiceID,  
        output_format="mp3_22050_32",
        text=text,
        model_id="eleven_turbo_v2",  # use the turbo model for low latency, for other languages use the `eleven_multilingual_v2`
        voice_settings=VoiceSettings(
            stability=0.0,
            similarity_boost=1.0,
            style=0.0,
            use_speaker_boost=True,
        ),
    )

    # Generating a unique file name for the output MP3 file
    save_file_path = f"Voice/elevenlabs_speech.mp3"
    # Writing the audio stream to the file

    with open(save_file_path, "wb") as f:
        for chunk in response:
            if chunk:
                f.write(chunk)
    playsound(save_file_path)
    print(f"A new audio file was saved successfully at {save_file_path}")
    return save_file_path
   

def generate_elevenlabs_pi_audio(text: str) -> str:

    # Calling the text_to_speech conversion API with detailed parameters
    response = client.text_to_speech.convert(
        voice_id=elevenLabs_bogle_voiceID,  
        output_format="mp3_22050_32",
        text=text,
        model_id="eleven_turbo_v2",  # use the turbo model for low latency, for other languages use the `eleven_multilingual_v2`
        voice_settings=VoiceSettings(
            stability=0.0,
            similarity_boost=1.0,
            style=0.0,
            use_speaker_boost=True,
        ),
    )

    # Generating a unique file name for the output MP3 file
    save_file_path = f"Voice/elevenlabs_speech.mp3"
    # Writing the audio stream to the file

    with open(save_file_path, "wb") as f:
        for chunk in response:
            if chunk:
                f.write(chunk)
    
    try:
        # Initialize the mixer module
        pygame.mixer.init()
        # Load the MP3 file
        pygame.mixer.music.load(save_file_path)
        # Play the music
        pygame.mixer.music.play()
        print(f"Playing audio file: {save_file_path}")
        # Wait until the music finishes playing
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    except Exception as e:
        print(f"Error playing audio: {e}")
    finally:
        # Quit the mixer to free resources
        pygame.mixer.quit()

    print(f"A new audio file was saved successfully at {save_file_path}")
    return save_file_path
   
