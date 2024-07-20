from faster_whisper import WhisperModel

# Function to transcribe the recorded audio using faster-whisper
def transcribe_with_whisper_Mac(audio_file):

    print(f"transcribe_with_whisper file")

    model_size = "small.en"

    # Using int8 for better performance on M1
    whisper_model = WhisperModel(model_size, compute_type="int8")
    #whisper_model = WhisperModel(model_size, compute_type="auto")


    segments, info = whisper_model.transcribe(audio_file, beam_size=5)
    transcription = ""
    for segment in segments:
        transcription += segment.text + " "

    print(transcription)
    return transcription.strip()


# Function to transcribe the recorded audio using faster-whisper
def transcribe_with_whisper_Pi(audio_file):

    print(f"transcribe_with_whisper file")

    model_size = "tiny.en"

    # Using int8 for better performance on M1
    whisper_model = WhisperModel(model_size, compute_type="int8")
    #whisper_model = WhisperModel(model_size, compute_type="auto")


    segments, info = whisper_model.transcribe(audio_file, beam_size=5)
    transcription = ""
    for segment in segments:
        transcription += segment.text + " "

    print(transcription)
    return transcription.strip()


