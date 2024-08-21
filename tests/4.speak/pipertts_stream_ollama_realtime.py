#  Not working

import time
import openai
from RealtimeTTS import TextToAudioStream
from piper.voice import PiperVoice
import pyaudio
import numpy as np
import sounddevice as sd

# Setup PiperTTS
voicedir = "pipertts/"  # Directory where the ONNX model files are stored
model = voicedir + "en_US-norman-medium.onnx"
config = voicedir + "en_en_US_norman_medium_en_US-norman-medium.onnx.json"  # Correct config file name

# PiperVoiceEngineWrapper Definition
class PiperVoiceEngineWrapper:
    def __init__(self):
        try:
            # Load the Piper model and wrap it with PiperVoiceEngineWrapper
            voice = PiperVoice.load(model, config)
            self.piper_voice = voice
            self.format = pyaudio.paInt16  # Example format (16-bit audio)
            self.channels = 1  # Mono audio
            # self.rate = 16000 
            self.rate = voice.config.sample_rate
            self.engine_name = "PiperTTS" 
        except Exception as e:
            print(f"Error loading Piper model: {e}")
            raise e

    def get_stream_info(self):
        return self.format, self.channels, self.rate

    def synthesize(self, text):
        try:
            print(f"Synthesizing text: {text}")
            # Synthesize the audio in a streaming fashion
            for audio_bytes in self.piper_voice.synthesize_stream_raw(text):
                int_data = np.frombuffer(audio_bytes, dtype=np.int16)
                yield int_data
        except Exception as e:
            print(f"Error during synthesis: {e}")

    def can_consume_generators(self):
        return True

    def set_muted(self, muted):
        pass  # Implement muting if necessary

# Initialize OpenAI and ElevenLabs clients
openai_client = openai.OpenAI(base_url='http://localhost:11434/v1', api_key='ollama')

# Initialize the voice engine
voice_engine = PiperVoiceEngineWrapper()

# Define user input and system message
user_input = "Who painted the Mona Lisa?"
system_message = "You are a helpful assistant and keep response as 1 sentence and keep it short."

# Prepare messages for OpenAI API
messages = [{"role": "system", "content": system_message}, {"role": "user", "content": user_input}]

def on_audio_chunk_callback(chunk):
    print(f"Chunk received, len: {len(chunk)}")

def text_start():
    print("[TEXT START]", end="", flush=True)

def text_stop():
    print("[TEXT STOP]", end="", flush=True)

def audio_start():
    print("[AUDIO START]", end="", flush=True)

def audio_stop():
    print("[AUDIO STOP]", end="", flush=True)

# Initialize TextToAudioStream with the Piper engine
stream = TextToAudioStream(
    voice_engine,
    on_text_stream_start=text_start, 
    on_text_stream_stop=text_stop, 
    on_audio_stream_start=audio_start, 
    on_audio_stream_stop=audio_stop,
    log_characters=True
)

# Function to stream text from OpenAI
def streamdata():
    # Streamed completion for OpenAI response
    streamed_completion = openai_client.chat.completions.create(
        model="tinyllama",
        messages=messages,
        stream=True
    )

    # Yield each chunk to PiperTTS
    for chunk in streamed_completion:
        if "content" in chunk.choices[0].delta:
            text_chunk = chunk.choices[0].delta["content"]
            yield text_chunk

def main():
    print("Starting...")
    test = streamdata()
    
    # Feed text to the stream and play it asynchronously
    try:
        stream.feed(test)
        stream.play_async()

        # Keeping the main thread alive while the audio plays asynchronously
        while stream.is_playing():
            time.sleep(0.1)
    except Exception as e:
        print(f"Error during streaming and playback: {e}")

if __name__ == "__main__":
    main()
