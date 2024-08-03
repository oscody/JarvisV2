import pyaudio
import wave
import time
from faster_whisper import WhisperModel
import numpy as np
import os

# Define variables
model_size = "small.en"
duration = 5  # Duration of recording in seconds
format = pyaudio.paInt16
channels = 1
rate = 16000
frames_per_buffer = 1024

# Initialize PyAudio
p = pyaudio.PyAudio()

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "../../voice_recording/recording_whisper_test.wav")

def record_and_transcribe_without_file():
    # Start overall timer
    start_time = time.time()
    frames = []

    print("Recording without saving to file...")

    # Open stream
    stream = p.open(format=format, channels=channels, rate=rate, input=True, frames_per_buffer=frames_per_buffer)
    # Record audio for the specified duration
    start_record_time = time.time()
    while time.time() - start_record_time < duration:
        data = stream.read(frames_per_buffer)
        frames.append(data)

    print("Recording stopped.")

    # Stop and close the stream
    stream.stop_stream()
    stream.close()

    # Convert frames to numpy array
    audio_data = np.frombuffer(b''.join(frames), dtype=np.int16)

    # Initialize Whisper model
    whisper_model = WhisperModel(model_size, compute_type="int8")

    # Transcribe the audio data
    segments, info = whisper_model.transcribe(audio_data, beam_size=5)
    transcription = "".join(segment.text for segment in segments)

    # End overall timer
    end_time = time.time()
    print("Transcription:", transcription.strip())
    print(f"Total execution time (without saving to file): {end_time - start_time:.2f} seconds\n")


def record_and_transcribe_with_file():
    # Start overall timer
    start_time = time.time()
    frames = []

    print("Recording and saving to file...")

    # Open stream
    stream = p.open(format=format, channels=channels, rate=rate, input=True, frames_per_buffer=frames_per_buffer)
    # Record audio for the specified duration
    start_record_time = time.time()
    while time.time() - start_record_time < duration:
        data = stream.read(frames_per_buffer)
        frames.append(data)

    print("Recording stopped.")

    # Stop and close the stream
    stream.stop_stream()
    stream.close()

    # Save the recorded audio to a WAV file
    with wave.open(file_path, 'wb') as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(p.get_sample_size(format))
        wf.setframerate(rate)
        wf.writeframes(b''.join(frames))

    # Initialize Whisper model
    whisper_model = WhisperModel(model_size, compute_type="int8")

    # Transcribe the audio file
    segments, info = whisper_model.transcribe(file_path, beam_size=5)
    transcription = "".join(segment.text for segment in segments)

    # End overall timer
    end_time = time.time()
    print("Transcription:", transcription.strip())
    print(f"Total execution time (with saving to file): {end_time - start_time:.2f} seconds\n")


# Run tests for both methods
record_and_transcribe_without_file()
record_and_transcribe_with_file()

# Terminate PyAudio instance
p.terminate()
