import wave
import json
import os
from piper.voice import PiperVoice
from piper.config import PiperConfig  # Hypothetical import, replace with actual if different


# Load the model and config
model = "pipertts/en_US-norman-medium.onnx"
config_path = "pipertts/en_en_US_norman_medium_en_US-norman-medium.onnx.json"

# # Debugging prints
# print("Current working directory:", os.getcwd())
# print("Model path:", model)
# print("Config path:", config_path)

# Load the config as a dictionary
# Load the config using the PiperConfig class
with open(config_path, 'r') as config_file:
    config_dict = json.load(config_file)
    config = PiperConfig(**config_dict)  # Hypothetical constructor, replace with actual if different


voice = PiperVoice(model, config)
text = "This is an example of text to speech"


print("sample",config['audio']['sample_rate'])


# Create a wave file object in write mode
with wave.open("output.wav", "w") as wav_file:
    # Set parameters for the wave file
    wav_file.setnchannels(1)  # Mono
    wav_file.setsampwidth(2)  # Sample width in bytes
    wav_file.setframerate(config['audio']['sample_rate'])  # Sample rate from the loaded config

    voice.synthesize(text, wav_file)
