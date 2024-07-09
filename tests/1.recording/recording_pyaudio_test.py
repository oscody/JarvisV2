import pyaudio
import time
import numpy as np

# Define variables
duration = 5  # Duration of recording in seconds
samplerate = 16000  # Sample rate
channels = 1
frames_per_buffer = 1024

# Initialize PyAudio
p = pyaudio.PyAudio()

# Open stream
stream = p.open(format=pyaudio.paFloat32, channels=channels, rate=samplerate, input=True, frames_per_buffer=frames_per_buffer)
frames = []

print("Recording...")

# Measure recording time
start_time = time.time()
for _ in range(0, int(samplerate / frames_per_buffer * duration)):
    data = stream.read(frames_per_buffer)
    frames.append(np.frombuffer(data, dtype=np.float32))
end_time = time.time()

print("Recording stopped.")

# Stop and close the stream
stream.stop_stream()
stream.close()
p.terminate()

# Calculate recording duration
recording_duration = end_time - start_time
print(f"PyAudio recording time: {recording_duration:.2f} seconds")
