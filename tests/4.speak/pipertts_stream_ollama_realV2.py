#  Not working

import time
import openai
from RealtimeTTS import TextToAudioStream
from piper.voice import PiperVoice
import pyaudio
import numpy as np
import threading
import queue
import sounddevice as sd

# Setup PiperTTS
voicedir = "pipertts/"  # Directory where the ONNX model files are stored
model = voicedir + "en_US-norman-medium.onnx"
config = voicedir + "en_en_US_norman_medium_en_US-norman-medium.onnx.json"  # Correct config file name


class PiperVoiceEngineWrapper:
    def __init__(self):
        try:
            # Load the Piper model
            self.piper_voice = PiperVoice.load(model, config)
            self.format = pyaudio.paInt16  # 16-bit audio format
            self.channels = 1  # Mono audio
            self.rate = self.piper_voice.config.sample_rate
            self.engine_name = "PiperTTS"
            self.stream_running = False
            self.muted = False
            self.playback_thread = None
            self.abort_event = threading.Event()
            self.audio_queue = queue.Queue()
        except Exception as e:
            print(f"Error loading Piper model: {e}")
            raise e

    def get_stream_info(self):
        return self.format, self.channels, self.rate

    def synthesize(self, text):
        try:
            # Ensure that text is a string before phonemization
            if isinstance(text, str):
                print(f"Synthesizing text: {text}")
                # Synthesize the audio in a streaming fashion
                for audio_bytes in self.piper_voice.synthesize_stream_raw(text):
                    int_data = np.frombuffer(audio_bytes, dtype=np.int16)
                    yield int_data
            else:
                print(f"Invalid input type for synthesis: {type(text)}")
        except Exception as e:
            print(f"Error during synthesis: {e}")


    def can_consume_generators(self):
        return True

    def set_muted(self, muted):
        self.muted = muted

    def stop(self):
        self.abort_event.set()
        if self.playback_thread is not None and self.playback_thread.is_alive():
            self.playback_thread.join()

    def play(self):
        if not self.muted:
            self.stream_running = True
            while not self.audio_queue.empty() and not self.abort_event.is_set():
                audio_data = self.audio_queue.get()
                sd.play(audio_data, samplerate=self.rate)
                sd.wait()

        self.stream_running = False

    def play_async(self):
        if not self.stream_running:
            self.playback_thread = threading.Thread(target=self.play)
            self.playback_thread.start()

    def is_playing(self):
        return self.stream_running


# Initialize OpenAI API client
openai_client = openai.OpenAI(base_url='http://localhost:11434/v1', api_key='ollama')

# Initialize the voice engine
voice_engine = PiperVoiceEngineWrapper()

# Define user input and system message
user_input = "Who painted the Mona Lisa?"
system_message = "You are a helpful assistant and keep response as 1 sentence and keep it short."

# Prepare messages for OpenAI API
messages = [{"role": "system", "content": system_message}, {"role": "user", "content": user_input}]

# Callbacks for streaming events
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

def dummy_generator():
        yield "Hey guys! "
        yield "These here are "
        yield "realtime spoken words "
        yield "based on openai "
        yield "tts text synthesis."

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
    # test = streamdata()
    # test = dummy_generator()

    # Feed text to the stream and play it asynchronously
    try:
        stream.feed(dummy_generator())
        stream.play_async()

        # Keeping the main thread alive while the audio plays asynchronously
        while stream.is_playing():
            time.sleep(0.1)
    except Exception as e:
        print(f"Error during streaming and playback: {e}")
    finally:
        voice_engine.stop()

if __name__ == "__main__":
    main()
