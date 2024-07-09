Begin


python3 -m venv JarvisV2
source JarvisV2/bin/activate

tree -I "JarvisV2"



pygame vs pyaudio vs sounddevice


pyaudio slightly faster 

1. recording - pyaudio faster

5.01 seconds - python tests/1.recording/recording_pyaudio_test.py

5.26 seconds - python tests/1.recording/recording_sounddevice_test.py

2. 

python tests/2.transcibe/whisper_raw_audio_test.py


python tests/2.transcibe/whisper_file_audio_test.py


python tests/2.transcibe/whisper_from_file_audio_test.py