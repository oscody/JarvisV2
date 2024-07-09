#file to test recording to the whisper without saving to file

import pyaudio
import time
from faster_whisper import WhisperModel
import numpy as np

# Define variables
model_size = "small.en"
duration = 5  # duration of recording in seconds


# Start overall timer
start_time = time.time()

# Initialize PyAudio
p = pyaudio.PyAudio()

# Open stream
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=1024)
frames = []

print("Recording...")

# Record audio for the specified duration
start_record_time = time.time()
while time.time() - start_record_time < duration:
    data = stream.read(1024)
    frames.append(data)

print("Recording stopped.")

# Stop and close the stream
stream.stop_stream()
stream.close()
p.terminate()

# Convert frames to numpy array
audio_data = np.frombuffer(b''.join(frames), dtype=np.int16)

# Initialize Whisper model
whisper_model = WhisperModel(model_size, compute_type="int8")

# Transcribe the audio data
segments, info = whisper_model.transcribe(audio_data, beam_size=5)
transcription = ""
for segment in segments:
    transcription += segment.text + " "

print("Transcription:")
print(transcription.strip())


# End overall timer
end_time = time.time()
print(f"Total execution time: {end_time - start_time:.2f} seconds")