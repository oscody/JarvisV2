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


# Initialize Whisper model
whisper_model = WhisperModel(model_size,device="cpu", compute_type="int8")

# Record audio for the specified duration
start_record_time = time.time()

try:
    while time.time() - start_record_time < duration:
        data = stream.read(CHUNK_SIZE)
        numpy_data = np.frombuffer(data, dtype=np.int16).astype(np.float32) / 32768.0
        
        if np.isnan(numpy_data).any():
            print("Warning: NaN values encountered in audio data, skipping this chunk.")
            continue

        segments, info = whisper_model.transcribe(numpy_data, beam_size=5, language="en")

        print("Transcription:")
        for segment in segments:
            print("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))

except KeyboardInterrupt:
    print("Stopping...")

finally:
    stream.stop_stream()
    stream.close()
    p.terminate()
    print("Stopping...")


# End overall timer
end_time = time.time()
print(f"model size,{model_size} --- Total execution time: {end_time - start_time:.2f} seconds")