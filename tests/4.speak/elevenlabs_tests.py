import os
import time
import uuid
from dotenv import load_dotenv
from elevenlabs import VoiceSettings
from elevenlabs.client import ElevenLabs
from pydub import AudioSegment
import simpleaudio as sa
from playsound import playsound

load_dotenv()

ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")

if not ELEVENLABS_API_KEY:
    raise ValueError("ELEVENLABS_API_KEY environment variable not set")

client = ElevenLabs(api_key=ELEVENLABS_API_KEY)

def text_to_speech_file(text: str, filename: str) -> str:
    """
    Converts text to speech and saves the output as an MP3 file.

    Args:
        text (str): The text content to convert to speech.
        filename (str): The name of the output file.

    Returns:
        str: The file path where the audio file has been saved.
    """
    # Calling the text-to-speech conversion API
    response = client.text_to_speech.convert(
        voice_id="N2lVS1w4EtoT3dr4eOWO",  # Adam pre-made voice
        optimize_streaming_latency="0",
        output_format="mp3_22050_32",
        text=text,
        model_id="eleven_turbo_v2",
        voice_settings=VoiceSettings(
            stability=0.0,
            similarity_boost=1.0,
            style=0.0,
            use_speaker_boost=True,
        ),
    )

    # Generating a unique file name for the output MP3 file
    mp3_file_path = f"Voice/{filename}.mp3"
    wav_file_path = f"Voice/{filename}.wav"
    
    # Writing the audio stream to the file
    os.makedirs(os.path.dirname(mp3_file_path), exist_ok=True)
    with open(mp3_file_path, "wb") as f:
        for chunk in response:
            if chunk:
                f.write(chunk)

    print(f"A new audio file was saved successfully at {mp3_file_path}")

    # Convert MP3 to WAV if using simpleaudio
    sound = AudioSegment.from_mp3(mp3_file_path)
    sound.export(wav_file_path, format="wav")
    print(f"Converted to WAV format at {wav_file_path}")

    return mp3_file_path, wav_file_path

def test_playback_speed():
    text = "If no one is around you Say baby I love you If you ain't runnin' game"

    # Generate audio files
    mp3_file, wav_file = text_to_speech_file(text, "elevenlabs_test")

    # Test simpleaudio
    start_time = time.time()
    wave_obj = sa.WaveObject.from_wave_file(wav_file)
    play_obj = wave_obj.play()
    play_obj.wait_done()  # Wait until the sound has finished playing
    simpleaudio_time = time.time() - start_time

    # Test playsound
    start_time = time.time()
    playsound(mp3_file)
    playsound_time = time.time() - start_time

    print(f"Simpleaudio playback time: {simpleaudio_time:.4f} seconds")
    print(f"Playsound playback time: {playsound_time:.4f} seconds")

if __name__ == "__main__":
    test_playback_speed()
