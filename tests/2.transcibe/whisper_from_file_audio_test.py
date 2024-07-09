import pyaudio
import wave
import time
from faster_whisper import WhisperModel
import os


# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# 
# print("path",script_dir)

# Define the file path relative to the script's directory
file_path = os.path.join(script_dir, "../../voice_recording/chicken_test.mp3")
# print("file_path",file_path)

audio_file = file_path  # Path to the audio file to be transcribed

# Define variables
model_size = "small.en"
duration = 5  # Duration of recording in seconds

print("model size",model_size)


# Start overall timer
start_time = time.time()




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
print(f"model size,{model_size} --- Total execution time: {end_time - start_time:.2f} seconds")