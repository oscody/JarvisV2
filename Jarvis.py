import os

import speech_to_text_service as transcribe
import play_service as play
import record_service as rec


voicefolder = "voice_recording"

audio_file = os.path.join(voicefolder, "temp_recording.wav")

def jarvis():

    try:

        while True:

            rec.record_audio(audio_file)
            user_input = transcribe.transcribe_with_whisper(audio_file)
            play.play_audio(audio_file)


    except KeyboardInterrupt:
        print("\nStopping...")



jarvis()  # Start the conversation



