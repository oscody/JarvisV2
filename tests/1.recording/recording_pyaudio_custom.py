import pyaudio
import wave
import tempfile
import math
import struct
import simpleaudio as sa


# Audio parameters
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
THRESHOLD = 1000  # Silence threshold
SILENCE_DURATION = 1  # Seconds of silence to signify end of command


def is_silent(data_chunk):
    """Check if the given audio chunk is silent."""
    rms = math.sqrt(sum(
        sample ** 2 for sample in struct.unpack("<" + "h" * (len(data_chunk) // 2), data_chunk)
    ) / len(data_chunk))
    return rms < THRESHOLD

def record_until_pause():
    """Record audio from the microphone until a pause is detected."""
    print("Listening... Speak now.")
    audio = pyaudio.PyAudio()
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)

    frames = []
    silent_chunks = 0
    silent_chunks_threshold = int(SILENCE_DURATION * RATE / CHUNK)
    started = False

    while True:
        data = stream.read(CHUNK, exception_on_overflow=False)
        is_silence = is_silent(data)

        if not started:
            if not is_silence:
                started = True
                frames.append(data)
        else:
            frames.append(data)
            if is_silence:
                silent_chunks += 1
            else:
                silent_chunks = 0

            if silent_chunks > silent_chunks_threshold:
                break

    stream.stop_stream()
    stream.close()
    audio.terminate()

    if not frames:
        print("No speech detected.")
        return None

    temp_audio = tempfile.NamedTemporaryFile(delete=False, suffix='.wav')
    with wave.open(temp_audio.name, 'wb') as wave_file:
        wave_file.setnchannels(CHANNELS)
        wave_file.setsampwidth(audio.get_sample_size(FORMAT))
        wave_file.setframerate(RATE)
        wave_file.writeframes(b''.join(frames))

    return temp_audio.name

while True:
    audio_path = record_until_pause()
    print(f"Done path {audio_path}")
    break