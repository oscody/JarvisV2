import os
from dotenv import load_dotenv
from elevenlabs import VoiceSettings
from elevenlabs.client import ElevenLabs
import pygame

load_dotenv()

ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
elevenLabs_bogle_voiceID = os.getenv("elevenLabs_bogle_voiceID")

if not ELEVENLABS_API_KEY:
    raise ValueError("ELEVENLABS_API_KEY environment variable not set")

client = ElevenLabs(
    api_key=ELEVENLABS_API_KEY,
)

def text_to_speech_file(text: str) -> str:
    # Calling the text_to_speech conversion API with detailed parameters
    response = client.text_to_speech.convert(
        voice_id=elevenLabs_bogle_voiceID,
        optimize_streaming_latency="0",
        output_format="mp3_22050_32",
        text=text,
        model_id="eleven_turbo_v2",  # Use the turbo model for low latency; for other languages use 'eleven_multilingual_v2'
        voice_settings=VoiceSettings(
            stability=0.0,
            similarity_boost=1.0,
            style=0.0,
            use_speaker_boost=True,
        ),
    )

    # Generating a unique file name for the output MP3 file
    save_file_path = "Voice/elevenlabs_pi_speech.mp3"

    # Ensure the directory exists
    os.makedirs(os.path.dirname(save_file_path), exist_ok=True)

    # Writing the audio stream to the file
    with open(save_file_path, "wb") as f:
        for chunk in response:
            if chunk:
                f.write(chunk)

    print(f"A new audio file was saved successfully at {save_file_path}")

    # Return the path of the saved audio file
    return save_file_path

def play_audio(file_path: str):
    try:
        # Initialize the mixer module
        pygame.mixer.init()
        # Load the MP3 file
        pygame.mixer.music.load(file_path)
        # Play the music
        pygame.mixer.music.play()
        print(f"Playing audio file: {file_path}")
        # Wait until the music finishes playing
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    except Exception as e:
        print(f"Error playing audio: {e}")
    finally:
        # Quit the mixer to free resources
        pygame.mixer.quit()

if __name__ == "__main__":
    # Convert text to speech and get the path to the audio file
    filepath = text_to_speech_file(
        "What did you say? You seem to love watching your show and you are not talking to me. Why?"
    )
    # Play the audio file using pygame
    play_audio(filepath)
