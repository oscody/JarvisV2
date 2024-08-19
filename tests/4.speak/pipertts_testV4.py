# working 

import wave
from piper.voice import PiperVoice

print("\Playing...audio")

voicedir = "pipertts/" # Where onnx model files are stored on my machine
model = voicedir + "en_US-norman-medium.onnx"
config = voicedir + "en_en_US_norman_medium_en_US-norman-medium.onnx.json" # Correct config file name

# Load the model and config
voice = PiperVoice.load(model, config)

text_to_speak = "This is an example of text to speech saying Where onnx model files are stored on my machine"

wav_file = wave.open("Voice/pipertts.wav", "w")
audio = voice.synthesize(text_to_speak, wav_file)