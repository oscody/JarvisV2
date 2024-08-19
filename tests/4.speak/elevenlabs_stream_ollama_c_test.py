# ollama_stream_elevenlabs_b_test


import time
import os
import tempfile
from io import BytesIO
from pydub import AudioSegment
from pydub.playback import play
import threading
import openai
from openai import OpenAI
from elevenlabs.client import ElevenLabs
from elevenlabs import play, save, stream, Voice, VoiceSettings


# Function to stream text from OpenAI to ElevenLabs
def openai_to_elevenlabs_stream():


    # Define user input and system message
    user_input = "Who painted the Mona Lisa?"
    system_message = "You are a helpful assistant and keep response as 1 sentence and keep it short."

    # Prepare messages for OpenAI API
    messages = [{"role": "system", "content": system_message}, {"role": "user", "content": user_input}]
    
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


# Initialize OpenAI and ElevenLabs clients
openai_client = OpenAI(base_url='http://localhost:11434/v1', api_key='ollama')
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
elevenlabs_client = ElevenLabs(api_key=ELEVENLABS_API_KEY)







generator = openai_to_elevenlabs_stream()

stream(elevenlabs_client.generate(text=generator, voice="Brian", model="eleven_monolingual_v1", stream=True))
