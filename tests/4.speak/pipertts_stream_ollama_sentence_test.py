import requests, pyaudio, time, pygame, threading, queue, tempfile
import soundfile as sf
from dotenv import load_dotenv
from openai import OpenAI
import os
from piper.voice import PiperVoice
import sounddevice as sd
import numpy as np

# Load environment variables
load_dotenv()

# Flag to check if the first audio has been played
is_first_audio_played = False

# Setup PiperTTS
voicedir = "pipertts/"  # Directory where the ONNX model files are stored
model = voicedir + "en_US-norman-medium.onnx"
config = voicedir + "en_en_US_norman_medium_en_US-norman-medium.onnx.json"  # Correct config file name

# Load the PiperVoice model and configuration
voice = PiperVoice.load(model, config)

# Initialize OpenAI and ElevenLabs clients
openai_client = OpenAI(base_url='http://localhost:11434/v1', api_key='ollama')


# Define user input and system message
user_input = "Who painted the Mona Lisa?"
system_message = "You are a helpful assistant and keep response as 1 sentence and keep it short."

# Prepare messages for OpenAI API
messages = [{"role": "system", "content": system_message}, {"role": "user", "content": user_input}]



def generate_and_play_audio(input_text):
    """Generate and stream audio directly without saving files."""
    try:
        # Setup a sounddevice OutputStream with appropriate parameters
        stream = sd.OutputStream(samplerate=voice.config.sample_rate, channels=1, dtype='int16')
        stream.start()

        # Stream and play the generated audio
        for audio_bytes in voice.synthesize_stream_raw(input_text):
            int_data = np.frombuffer(audio_bytes, dtype=np.int16)
            stream.write(int_data)

        stream.stop()
        stream.close()

    except Exception as e:
        print(f"Error during audio generation or playback: {e}")

def print_w_stream(message):
    """Stream the response from OpenAI and queue the sentences for audio playback."""

     # Streamed completion for OpenAI response
    completion = openai_client.chat.completions.create(
        model="tinyllama",
        messages=messages,
        stream=True
    )
    
    sentence = ''
    sentences = []
    sentence_end_chars = {'.', '?', '!', '\n'}

    # Stream and process the output
    for chunk in completion:
        content = chunk.choices[0].delta.content
        if content:
            for char in content:
                sentence += char
                if char in sentence_end_chars:
                    sentence = sentence.strip()
                    if sentence and sentence not in sentences:
                        sentences.append(sentence)
                        print(f"Queued sentence: {sentence}")  # Logging queued sentence
                        generate_and_play_audio(sentence)  # Directly generate and play audio
                    sentence = ''
    return sentences

# Prompt the user for input
# user_input = input("What do you want to ask the AI? ")

start_time = time.time()  # Record the start time

# Process the user input and generate audio responses
print_w_stream(user_input)

