# Not wOrking

# Text-To-Speech Translation with Piper TTS and Python 
# TechMakerAI on YouTube

from piper import PiperVoice
import wave  
from io import BytesIO
from pygame import mixer

mixer.init()


sampleRate = 22050

wavaudio = BytesIO()

model = "pipertts/en_US-norman-medium.onnx"
config_path = "pipertts/en_en_US_norman_medium_en_US-norman-medium.onnx.json"

voice = PiperVoice(model, config_path)

text = 'Hi,there,how can I help you? This is the second sentence of the paragraph. This is the third sentence of the paragraph. '
  
with wave.open(wavaudio, "wb") as wav_file:
    wav_file.setnchannels(1)  # Mono
    wav_file.setsampwidth(2)  # 2 bytes per sample
    wav_file.setframerate(sampleRate)  # Sample rate, you can adjust as needed

    voice.synthesize(text, wav_file)

wavaudio.seek(0)

mixer.music.load(wavaudio, "wav")
mixer.music.play()

while mixer.music.get_busy():
    pass

