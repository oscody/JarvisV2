import pyaudio
import time
import numpy as np



def record_audio(duration=5):

    CHUNK_SIZE = 16000
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 16000

    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK_SIZE)

    print("Recording...")

    start_time = time.time()
    while time.time() - start_time < duration:
        data = stream.read(CHUNK_SIZE)
        audio_data = np.frombuffer(data, dtype=np.int16).astype(np.float32) / 32768.0

    print("Recording stopped.")

    stream.stop_stream()
    stream.close()
    p.terminate()

    return audio_data


