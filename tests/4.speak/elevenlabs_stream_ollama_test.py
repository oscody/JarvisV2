import time
import openai
from openai import OpenAI
import os
from io import BytesIO
from elevenlabs import VoiceSettings
from elevenlabs.client import ElevenLabs
from pydub import AudioSegment
from pydub.playback import play
import tempfile
import threading

# Initialize OpenAI and ElevenLabs clients
openai_client = OpenAI(base_url='http://localhost:11434/v1', api_key='ollama')
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
elevenlabs_client = ElevenLabs(api_key=ELEVENLABS_API_KEY)

# Define user input and system message
user_input = "Who painted the Mona Lisa?"

system_message = "You are a helpful assistant and keep response as 1 sentence and keep it short"

# Prepare messages for OpenAI API
messages = [{"role": "system", "content": system_message}, {"role": "user", "content": user_input}]

# Define function to convert text to speech
def text_to_speech(text: str) -> BytesIO:
    response = elevenlabs_client.text_to_speech.convert(
        voice_id="pNInz6obpgDQGcFmaJgB",  # Adam pre-made voice
        output_format="mp3_22050_32",
        text=text,
        model_id="eleven_multilingual_v2",
        voice_settings=VoiceSettings(
            stability=0.0,
            similarity_boost=1.0,
            style=0.0,
            use_speaker_boost=True,
        ),
    )

    audio_stream = BytesIO()
    for chunk in response:
        if chunk:
            audio_stream.write(chunk)
    audio_stream.seek(0)
    return audio_stream

# Start the timer
start_time = time.time()

# Initialize variables
response_text = ""

# Function to play audio in a separate thread
def play_audio_stream(audio_stream):
    audio = AudioSegment.from_file(audio_stream, format="mp3")
    play(audio)

# Generate response from OpenAI API and stream TTS
with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_audio_file:
    for chunk in openai_client.chat.completions.create(
        model="tinyllama",
        messages=messages,
        stream=True
    ):
        content = chunk.choices[0].delta.content
        response_text += content
        # Stream text to speech
        audio_stream = text_to_speech(content)
        # Save to temp file
        with open(temp_audio_file.name, "ab") as f:
            f.write(audio_stream.read())

        # Play audio in a separate thread
        threading.Thread(target=play_audio_stream, args=(audio_stream,)).start()

# Stop the timer
end_time = time.time()
elapsed_time = end_time - start_time

# Print the response text and time taken
print(f"Response: {response_text}")
print(f"Time taken: {elapsed_time:.2f} seconds")

# Clean up temporary audio file
os.remove(temp_audio_file.name)
