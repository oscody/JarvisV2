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

------------------------------------------------------------------------------------------------------------------------------------------------

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

------------------------------------------------------------------------------------------------------------------------------------------------

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

