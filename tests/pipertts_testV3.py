# working 

import sounddevice as sd
import numpy as np
from piper.voice import PiperVoice

voicedir = "pipertts/" # Where onnx model files are stored on my machine
model = voicedir + "en_US-norman-medium.onnx"
config = voicedir + "en_en_US_norman_medium_en_US-norman-medium.onnx.json" # Correct config file name

# Load the model and config
voice = PiperVoice.load(model, config)

text = "This is an example of text to speech saying Where onnx model files are stored on my machine"

# Setup a sounddevice OutputStream with appropriate parameters
# The sample rate and channels should match the properties of the PCM data
stream = sd.OutputStream(samplerate=voice.config.sample_rate, channels=1, dtype='int16')
stream.start()

for audio_bytes in voice.synthesize_stream_raw(text):
    int_data = np.frombuffer(audio_bytes, dtype=np.int16)
    stream.write(int_data)

stream.stop()
stream.close()
