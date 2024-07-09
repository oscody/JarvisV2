#file to test recording to the whisper without saving to file

import pyaudio
import time
from faster_whisper import WhisperModel
import numpy as np

CHUNK_SIZE = 16000 * 5
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000


# Define variables
model_size = "tiny.en"
duration = 5  # duration of recording in seconds


# Start overall timer
start_time = time.time()

# Initialize PyAudio
p = pyaudio.PyAudio()

# Open stream
stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK_SIZE)


print("Recording...")

# Record audio for the specified duration
start_record_time = time.time()
while time.time() - start_record_time < duration:
    data = stream.read(CHUNK_SIZE)
    audio_data = np.frombuffer(data, dtype=np.int16).astype(np.float32) / 32768.0


print("Recording stopped.")

# Stop and close the stream
stream.stop_stream()
stream.close()
p.terminate()


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
print(f"model size,{model_size} --- Total execution time: {end_time - start_time:.2f} seconds")