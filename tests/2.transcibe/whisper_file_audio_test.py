import pyaudio
import wave
import time
from faster_whisper import WhisperModel
import os


# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

print("path",script_dir)

# Define the file path relative to the script's directory
file_path = os.path.join(script_dir, "../../voice_recording/recording_whisper_test.wav")
print("file_path",file_path)
audio_file = file_path  # Path to the audio file to be transcribed

# Define variables
model_size = "medium.en"
duration = 5  # Duration of recording in seconds



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

# Save the recorded audio to a WAV file
with wave.open(file_path, 'wb') as wf:
    wf.setnchannels(1)
    wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
    wf.setframerate(16000)
    wf.writeframes(b''.join(frames))

# Initialize Whisper model
whisper_model = WhisperModel(model_size, compute_type="int8")

# Transcribe the audio file
segments, info = whisper_model.transcribe(audio_file, beam_size=5)
transcription = ""
for segment in segments:
    transcription += segment.text + " "

print("Transcription:")
print(transcription.strip())


# End overall timer
end_time = time.time()
print(f"Total execution time: {end_time - start_time:.2f} seconds")