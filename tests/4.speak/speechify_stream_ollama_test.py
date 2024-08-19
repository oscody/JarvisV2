# Not working 

https://discord.com/channels/1232299860690993183/1232362721702449194/1270148695555444817
# getting an error


import requests
import aiofiles
import asyncio
import time
import os
from pydub import AudioSegment
from pydub.playback import play
import openai
from openai import OpenAI
from io import BytesIO

# Define the Speechify API configuration
API_BASE_URL = "https://api.sws.speechify.com"
API_KEY = os.getenv('speachifyAPI')  # Ensure this matches the key in your .env file
VOICE_ID = "george"

# Function to stream audio from Speechify API
async def stream_audio(text):
    response = requests.post(
        f"{API_BASE_URL}/v1/audio/stream",
        json={
            "input": f"<speak>{text}</speak>",
            "voice_id": VOICE_ID,
        },
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
            "Accept": "audio/mpeg"
        },
        stream=True
    )

    if not response.ok:
        raise Exception(f"{response.status_code} {response.reason}\n{response.text}")

    return response.iter_content(chunk_size=1024)

# Function to generate a response using OpenAI API
async def generate_response():
    user_input = "Who painted the Mona Lisa?"
    system_message = "You are a helpful assistant and keep response as 1 sentence and keep it short"

    # Initialize the OpenAI client with the API key
    client = OpenAI(base_url='http://localhost:11434/v1', api_key='ollama')

    messages = [{"role": "system", "content": system_message}] + [{"role": "user", "content": user_input}]

    # Start the timer
    start_time = time.time()

    streamed_completion = client.chat.completions.create(
        model="tinyllama",
        messages=messages,
        stream=True
    )

    # Extract and return the response
    response = ''
    for chunk in streamed_completion:
        response += chunk.choices[0].delta.content

    # Stop the timer
    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"Response: {response}")
    print(f"Time taken: {elapsed_time:.2f} seconds")

    return response

# Main function to generate a response and stream it as audio
async def main():
    # Generate the response from OpenAI API
    response_text = await generate_response()

    # Stream the generated response as audio
    audio_stream = await stream_audio(response_text)

    # Set up a buffer to collect the audio stream
    audio_buffer = BytesIO()

    # Collect the entire audio stream into the buffer
    for chunk in audio_stream:
        audio_buffer.write(chunk)

    # Rewind the buffer to the beginning
    audio_buffer.seek(0)

    # Load the complete audio data into an AudioSegment and play it
    audio_segment = AudioSegment.from_file(audio_buffer, format="mp3")
    play(audio_segment)

    # Save the audio to a file after streaming and playing
    async with aiofiles.open("speech.mp3", "wb") as f:
        await f.write(audio_buffer.getvalue())

    print("Audio successfully written to file.")

# Run the main function
if __name__ == "__main__":
    asyncio.run(main())
