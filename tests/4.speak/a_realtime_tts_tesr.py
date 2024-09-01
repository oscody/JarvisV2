import time
import os
from io import BytesIO
from pydub import AudioSegment
from pydub.playback import play
from openai import OpenAI
from elevenlabs.client import ElevenLabs
from elevenlabs import play, save, stream, Voice, VoiceSettings
from RealtimeTTS import TextToAudioStream, OpenAIEngine, ElevenlabsEngine
from scipy import stats
import numpy as np

# Initialize OpenAI and ElevenLabs clients
openai_client = OpenAI(base_url='http://localhost:11434/v1', api_key='ollama')
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
elevenlabs_client = ElevenLabs(api_key=ELEVENLABS_API_KEY)

# Prepare OpenAI and ElevenLabs engines
openai_engine = OpenAIEngine(model="tts-1", voice="nova")
elevenlabs_engine = ElevenlabsEngine(api_key=ELEVENLABS_API_KEY)

# Define user input and system message
user_input = "How long is a day?"
system_message = "You are a helpful assistant anaswer the question with very short consise response keep it to 1 sentence"

# Prepare messages for OpenAI API
messages = [{"role": "system", "content": system_message}, {"role": "user", "content": user_input}]

# Function to stream text from OpenAI to ElevenLabs
def openai_to_elevenlabs_stream():
    # Streamed completion for OpenAI response
    streamed_completion = openai_client.chat.completions.create(
        model="tinyllama",
        messages=messages,
        stream=True,
        temperature=0.1
    )

    response = ''
    # Yield each chunk to ElevenLabs
    for chunk in streamed_completion:
        content = chunk.choices[0].delta.content
        response += chunk.choices[0].delta.content
        print(f"Response: {response}")
        yield content

# Function to time the playback speed
def get_playback_time(engine):
    start_time = time.time()

    # Stream and play the audio
    stream = TextToAudioStream(engine)
    stream.feed(openai_to_elevenlabs_stream())  # Using the defined stream function
    stream.play()

    end_time = time.time()
    return end_time - start_time

# Collecting playback times
openai_playback_times = []
elevenlabs_playback_times = []

# Run the test multiple times for more accurate results
for i in range(2):  # Run 10 tests for each engine
    # OpenAI playback time
    openai_time = get_playback_time(openai_engine)
    openai_playback_times.append(openai_time)

    # ElevenLabs playback time
    elevenlabs_time = get_playback_time(elevenlabs_engine)
    elevenlabs_playback_times.append(elevenlabs_time)

# Perform independent t-test
t_stat, p_value = stats.ttest_ind(openai_playback_times, elevenlabs_playback_times)

print(f"T-statistic: {t_stat}")
print(f"P-value: {p_value}")

# Print average playback times for comparison
print(f"Average OpenAI playback time: {np.mean(openai_playback_times)} seconds")
print(f"Average ElevenLabs playback time: {np.mean(elevenlabs_playback_times)} seconds")
