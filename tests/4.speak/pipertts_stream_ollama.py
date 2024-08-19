# Not working yet have to 
#  Have to bring the sentences to gether to proccess before sendigng them off 
#  iterate over the loop for text in yield

import time
import os
import tempfile
from io import BytesIO
from pydub import AudioSegment
from pydub.playback import play

from openai import OpenAI


import sounddevice as sd
import numpy as np
from piper.voice import PiperVoice

# Initialize OpenAI and ElevenLabs clients
openai_client = OpenAI(base_url='http://localhost:11434/v1', api_key='ollama')


voicedir = "pipertts/" # Where onnx model files are stored on my machine
model = voicedir + "en_US-norman-medium.onnx"
config = voicedir + "en_en_US_norman_medium_en_US-norman-medium.onnx.json" # Correct config file name



# Load the model and config
voice = PiperVoice.load(model, config)

stream = sd.OutputStream(samplerate=voice.config.sample_rate, channels=1, dtype='int16')
stream.start()


# Define user input and system message
user_input = "Who painted the Mona Lisa?"
system_message = "You are a helpful assistant and keep response as 1 sentence and keep it short."

# Prepare messages for OpenAI API
messages = [{"role": "system", "content": system_message}, {"role": "user", "content": user_input}]

# Function to stream text from OpenAI to ElevenLabs
def think():
    # Streamed completion for OpenAI response
    streamed_completion = openai_client.chat.completions.create(
        model="tinyllama",
        messages=messages,
        stream=True
    )

    # Yield each chunk to ElevenLabs
    for chunk in streamed_completion:
        content = chunk.choices[0].delta.content
        print(f"Response: {content}")
        yield content


message = think()


# Access the values one by one
print(next(message))  # Output: first value
print(next(message))  # Output: second value
print(next(message))  # Output: third value




# for audio_bytes in voice.synthesize_stream_raw(text_to_synthesize):
#     int_data = np.frombuffer(audio_bytes, dtype=np.int16)
#     stream.write(int_data)


# print("\stoping...audio")

# stream.stop()
# stream.close()



