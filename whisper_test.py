
from faster_whisper import WhisperModel

audio_file = "Voice/Wolf.wav"

model_size = "medium.en"



whisper_model = WhisperModel(model_size, compute_type="int8")

# error on mac 
# whisper_model = WhisperModel(model_size, compute_type="float16")

# error on mac 
# whisper_model = WhisperModel(model_size, device="cuda", compute_type="float16")

# whisper_model = WhisperModel(model_size, device="cuda", compute_type="float16", num_workers=10)


segments, info = whisper_model.transcribe(audio_file, beam_size=5)
transcription = ""
for segment in segments:
    transcription += segment.text + " "

print(transcription.strip())