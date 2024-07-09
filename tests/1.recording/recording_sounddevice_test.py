import sounddevice as sd
import numpy as np
import time

# Define variables
duration = 5  # Duration of recording in seconds
samplerate = 16000  # Sample rate


print("Recording...")

# Measure recording time
start_time = time.time()
recording = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, blocking=True, dtype='float32')
end_time = time.time()

print("Recording stopped.")

# Calculate recording duration
recording_duration = end_time - start_time
print(f"Sounddevice recording time: {recording_duration:.2f} seconds")
