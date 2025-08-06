# JarvisV2 - Voice Assistant


python3 -m venv JarvisV2
source JarvisV2/bin/activate

pip install faster-whisper

tree -I "JarvisV2"

# Remove the old virtual environment
rm -rf JarvisV2

# Create new virtual environment with Python 3.10
python3.10 -m venv JarvisV2

# Activate the new environment
source JarvisV2/bin/activate

# Install dependencies
pip install -r requirements.txt

# Test that everything works
python test_environment.py

# Test Jarvis
python Jarvis.py


python V1/JarvisV1.2.py -- current best version - 8/4/24

## Dependencies

- openai
- torch
- faster-whisper
- PyAudio
- pygame
- sounddevice
- simpleaudio
- playsound
- soundfile
- pydub
- ollama
- elevenlabs
- python-dotenv

- `audioop_patch.py` provides missing audioop module
- All packages tested and working with Python 3.13.3


-ideas

pygame vs pyaudio vs sounddevice

1. recording - pyaudio faster - pyaudio slightly faster

5.01 seconds - python tests/1.recording/recording_pyaudio_test.py

5.26 seconds - python tests/1.recording/recording_sounddevice_test.py

---

2.STT

small model size

tiny model size -- works faster on raspberry pi

Pi --- from_file
small.en --- Total execution time: 56.53 seconds
tiny.en --- Total execution time: 14.92 seconds

python tests/2.transcibe/whisper_raw_audio_test.py

python tests/2.transcibe/whisper_file_audio_test.py

python tests/2.transcibe/whisper_from_file_audio_test.py

mac
Recording without saving to file...
Recording stopped.
Transcription: Thanks for watching!
Total execution time (without saving to file): 7.23 seconds

Recording and saving to file...
Recording stopped.
Transcription: to have. It might look weird to you, but how about I show you what my custom coat? Well...
Total execution time (with saving to file): 7.23 seconds

pi
Recording without saving to file...
Recording stopped.
Transcription: You know, no, no, no, no. No, no, no.
Total execution time (without saving to file): 24.87 seconds

Recording and saving to file...
Recording stopped.
Transcription: This is a weird set of things we have. If I look weird to you, but how about I show you what that cost don't go?
Total execution time (with saving to file): 7.92 seconds

---

4.TTS

ElevenLabs playsound not working on pi due to(pygobject)

pi
ElevenLabs playback time: 3.7715 seconds  
Speechify playback time: 3.4199 seconds
Piper playback time: 0.0001 seconds

mac
ElevenLabs playback time: 5.1008 seconds
Speechify playback time: 3.3685 seconds
Piper Not working on mac

testing piper tts on mac
Time to synthesize and write to file: 0.1903 seconds
Playsound playback time: 4.9927 seconds
Simpleaudio playback time: 5.0114 seconds
Sounddevice playback time (from file): 5.0628 seconds
Sounddevice synthesize and stream time: 5.2620 seconds

testing piper tts on Pi
Time taken to synthesize and write to file: 0.9798 seconds
Time taken to play back using simpleaudio: 5.0272 seconds
Time taken to play back using sounddevice (from file): 4.9452 seconds
Time taken to synthesize and stream audio using sounddevice: 5.9584 seconds
