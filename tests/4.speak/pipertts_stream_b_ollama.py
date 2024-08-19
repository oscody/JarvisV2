# import time
# import os
# import tempfile
# from io import BytesIO
# from pydub import AudioSegment
# from pydub.playback import play

# from openai import OpenAI


# import sounddevice as sd
# import numpy as np
# from piper.voice import PiperVoice

# # Initialize OpenAI and ElevenLabs clients
# openai_client = OpenAI(base_url='http://localhost:11434/v1', api_key='ollama')


# voicedir = "pipertts/" # Where onnx model files are stored on my machine
# model = voicedir + "en_US-norman-medium.onnx"
# config = voicedir + "en_en_US_norman_medium_en_US-norman-medium.onnx.json" # Correct config file name



# # Load the model and config
# voice = PiperVoice.load(model, config)

# stream = sd.OutputStream(samplerate=voice.config.sample_rate, channels=1, dtype='int16')
# stream.start()


# # Define user input and system message
# user_input = "Who painted the Mona Lisa?"
# system_message = "You are a helpful assistant and keep response as 1 sentence and keep it short."

# # Prepare messages for OpenAI API
# messages = [{"role": "system", "content": system_message}, {"role": "user", "content": user_input}]


#     # Streamed completion for OpenAI response
# streamed_completion = openai_client.chat.completions.create(
#     model="tinyllama",
#     messages=messages,
#     stream=True
# )

# # Yield each chunk to ElevenLabs
# for chunk in streamed_completion:
#     content = chunk.choices[0].delta.content
#     print(f"Response: {content}")

#     for audio_bytes in voice.synthesize_stream_raw(content):
#         int_data = np.frombuffer(audio_bytes, dtype=np.int16)
#         stream.write(int_data)

    


        


# stream.stop()
# stream.close()

# print("\stoping...audio")



# Working but sound horbile


import time
import os
import tempfile
from io import BytesIO
from pydub import AudioSegment
from pydub.playback import play

import sounddevice as sd
import numpy as np
from piper.voice import PiperVoice
from openai import OpenAI

# Initialize OpenAI client
openai_client = OpenAI(base_url='http://localhost:11434/v1', api_key='ollama')

# Define the model and configuration paths for PiperVoice
voicedir = "pipertts/"  # Directory where model files are stored
model = voicedir + "en_US-norman-medium.onnx"
config = voicedir + "en_en_US_norman_medium_en_US-norman-medium.onnx.json"  # Corrected config file name

# Load the model and config
voice = PiperVoice.load(model, config)

# Open an output stream for audio playback
stream = sd.OutputStream(samplerate=voice.config.sample_rate, channels=1, dtype='int16')
stream.start()

# Define user input and system message
user_input = "Who painted the Mona Lisa?"
system_message = "You are a helpful assistant and keep responses as 1 sentence and keep it short."

# Prepare messages for the OpenAI API
messages = [
    {"role": "system", "content": system_message},
    {"role": "user", "content": user_input}
]

# Streamed completion for OpenAI response
try:
    streamed_completion = openai_client.chat.completions.create(
        model="tinyllama",
        messages=messages,
        stream=True
    )

    # Process each chunk from the streamed completion
    for chunk in streamed_completion:
        content = chunk.choices[0].delta.content

        if content:
            print(f"Response: {content}")

            # Generate and play the synthesized audio for the response
            for audio_bytes in voice.synthesize_stream_raw(content):
                int_data = np.frombuffer(audio_bytes, dtype=np.int16)
                stream.write(int_data)

finally:
    # Ensure that the stream is stopped and closed properly
    stream.stop()
    stream.close()

    print("Stopping...audio playback")


