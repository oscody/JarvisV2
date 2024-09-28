import pyaudio
import wave
import math
import struct
import simpleaudio as sa
import os

# Audio parameters
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
THRESHOLD = 1000  # Silence threshold
SILENCE_DURATION = 1  # Seconds of silence to signify end of command

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

print("path",script_dir)

# Define the file path relative to the script's directory
file_path = os.path.join(script_dir, "../../voice_recording/")
print("file_path",file_path)
file_path  # Path to the audio file to be transcribed

# Define a unique filename for each recording
file_name = "detect_silence_pyaudio_custom.wav"
file_path = os.path.join(file_path, file_name)


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

    with wave.open(file_path, 'wb') as wave_file:
        wave_file.setnchannels(CHANNELS)
        wave_file.setsampwidth(audio.get_sample_size(FORMAT))
        wave_file.setframerate(RATE)
        wave_file.writeframes(b''.join(frames))

    return file_path

while True:
    audio_path = record_until_pause()
    print(f"Done path {audio_path}")
    break