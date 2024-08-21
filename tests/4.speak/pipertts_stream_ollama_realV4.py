#  Not working

import time
import openai
from piper.voice import PiperVoice
import numpy as np
import threading
import queue
import sounddevice as sd

# Setup PiperTTS
voicedir = "pipertts/"
model = voicedir + "en_US-norman-medium.onnx"
config = voicedir + "en_en_US_norman_medium_en_US-norman-medium.onnx.json"

class PiperVoiceEngineWrapper:
    def __init__(self):
        try:
            print("Loading Piper model...")
            self.piper_voice = PiperVoice.load(model, config)
            print("Piper model loaded successfully.")
            self.channels = 2  # Mono audio
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

    def synthesize(self, text):
        try:
            if isinstance(text, str):
                print(f"Synthesizing text: {text}")
                for audio_bytes in self.piper_voice.synthesize_stream_raw(text):
                    print("Audio chunk generated.")
                    int_data = np.frombuffer(audio_bytes, dtype=np.int16)
                    yield int_data
            else:
                print(f"Invalid input type for synthesis: {type(text)}")
        except Exception as e:
            print(f"Error during synthesis: {e}")

    def play_async(self):
        if not self.stream_running:
            print("Starting playback thread...")
            self.stream_running = True
            self.playback_thread = threading.Thread(target=self.play)
            self.playback_thread.start()

    def play(self):
        print("Opening audio stream...")
        # Specify device=1 to select MacBook Pro Speakers
        with sd.OutputStream(device=1, samplerate=self.rate, channels=self.channels, dtype='int16') as stream:
            while not self.audio_queue.empty() and not self.abort_event.is_set():
                audio_data = self.audio_queue.get()
                print("Writing audio data to stream.")
                stream.write(audio_data)
        print("Playback finished.")
        self.stream_running = False

    def stop(self):
        self.abort_event.set()
        if self.playback_thread is not None and self.playback_thread.is_alive():
            self.playback_thread.join()

    def is_playing(self):
        return self.stream_running

# Dummy generator for testing
def dummy_generator():
    yield "Hey guys! "
    yield "These here are "
    yield "realtime spoken words "
    yield "based on openai "
    yield "tts text synthesis."

def main():
    print("Starting...")
    voice_engine = PiperVoiceEngineWrapper()

    def generate_audio():
        for text_chunk in dummy_generator():
            for audio_chunk in voice_engine.synthesize(text_chunk):
                print("Audio chunk placed in queue.")
                voice_engine.audio_queue.put(audio_chunk)
        voice_engine.play_async()

    generate_audio_thread = threading.Thread(target=generate_audio)
    generate_audio_thread.start()

    while voice_engine.is_playing():
        time.sleep(0.1)

    generate_audio_thread.join()
    print("Stopping audio...")
    voice_engine.stop()

if __name__ == "__main__":
    main()
