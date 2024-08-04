import os
from dotenv import load_dotenv
import pvporcupine
import struct
import pyaudio

load_dotenv()

print(os.getenv('picovoice'))
ACCESS_KEY = os.getenv('picovoice')


keyWordPathPi = os.getenv('keyWordPathPi')
keyWordPathMac = os.getenv('keyWordPathMac')


def detection_wake_word(platform):
    porcupine = None
    pa = None
    audio_stream = None

    if platform == "Mac":
        KEYWORD_PATH = keyWordPathMac
    elif platform == "Pi":
        KEYWORD_PATH = keyWordPathPi


    try:
        porcupine = pvporcupine.create(
            access_key=ACCESS_KEY,
            keyword_paths=[KEYWORD_PATH]
        )
        
        pa = pyaudio.PyAudio()

        audio_stream = pa.open(
            rate=porcupine.sample_rate,
            channels=1,
            format=pyaudio.paInt16,
            input=True,
            frames_per_buffer=porcupine.frame_length)

        while True:
            pcm = audio_stream.read(porcupine.frame_length, exception_on_overflow=False)
            pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)

            result = porcupine.process(pcm)

            if result >= 0:
                print("Wake word detected!")
                return True

    finally:
        if audio_stream is not None:
            audio_stream.close()

        if pa is not None:
            pa.terminate()

        if porcupine is not None:
            porcupine.delete()