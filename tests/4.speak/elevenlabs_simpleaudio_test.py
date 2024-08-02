import os
import uuid
from dotenv import load_dotenv
from elevenlabs import VoiceSettings
from elevenlabs.client import ElevenLabs
from pydub import AudioSegment
import simpleaudio as sa

load_dotenv()

ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")

if not ELEVENLABS_API_KEY:
    raise ValueError("ELEVENLABS_API_KEY environment variable not set")

client = ElevenLabs(api_key=ELEVENLABS_API_KEY)

def text_to_speech_file(text: str) -> str:
    """
    Converts text to speech and saves the output as an MP3 file.

    This function uses a specific client for text-to-speech conversion. It configures
    various parameters for the voice output and saves the resulting audio stream to an
    MP3 file with a unique name.

    Args:
        text (str): The text content to convert to speech.

    Returns:
        str: The file path where the audio file has been saved.
    """
    # Calling the text-to-speech conversion API with detailed parameters
    response = client.text_to_speech.convert(
        voice_id="N2lVS1w4EtoT3dr4eOWO",  # Adam pre-made voice
        optimize_streaming_latency="0",
        output_format="mp3_22050_32",
        text=text,
        model_id="eleven_turbo_v2",  # use the turbo model for low latency, for other languages use the `eleven_multilingual_v2`
        voice_settings=VoiceSettings(
            stability=0.0,
            similarity_boost=1.0,
            style=0.0,
            use_speaker_boost=True,
        ),
    )

    # Generating a unique file name for the output MP3 file
    mp3_file_path = f"Voice/elevenlabs_speech_simpleaudio.mp3"
    wav_file_path = f"Voice/elevenlabs_speech_simpleaudio.wav"
    
    # Writing the audio stream to the file
    with open(mp3_file_path, "wb") as f:
        for chunk in response:
            if chunk:
                f.write(chunk)

    print(f"A new audio file was saved successfully at {mp3_file_path}")

    # Convert MP3 to WAV
    sound = AudioSegment.from_mp3(mp3_file_path)
    sound.export(wav_file_path, format="wav")
    print(f"Converted to WAV format at {wav_file_path}")

    # Return the path of the saved WAV file
    return wav_file_path

if __name__ == "__main__":
    filepath = text_to_speech_file("Hello Angelina, when are you coming to see me?")
    
    # Play the WAV file using simpleaudio
    wave_obj = sa.WaveObject.from_wave_file(filepath)
    play_obj = wave_obj.play()
    play_obj.wait_done()  # Wait until the sound has finished playing
