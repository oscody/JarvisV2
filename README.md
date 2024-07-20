Begin

openai
torch 


python3 -m venv JarvisV2
source JarvisV2/bin/activate

pip install faster-whisper

tree -I "JarvisV2"



pygame vs pyaudio vs sounddevice

1. recording - pyaudio faster - pyaudio slightly faster 

5.01 seconds - python tests/1.recording/recording_pyaudio_test.py

5.26 seconds - python tests/1.recording/recording_sounddevice_test.py


2. 

small model size

tiny model size -- works faster on raspberry pi 

Pi --- from_file
small.en --- Total execution time: 56.53 seconds
tiny.en --- Total execution time: 14.92 seconds


python tests/2.transcibe/whisper_raw_audio_test.py

python tests/2.transcibe/whisper_file_audio_test.py

python tests/2.transcibe/whisper_from_file_audio_test.py