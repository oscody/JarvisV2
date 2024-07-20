import os

import speech_to_text_service as transcribe
import play_service as play
import record_service as rec
import ai_service as ai
import text_to_speech_service as convert


voicefolder = "voice_recording"

audio_file = os.path.join(voicefolder, "temp_recording.wav")

def jarvis():

    try:

        while True:

            rec.record_audio(audio_file)
            user_input = transcribe.transcribe_with_whisper(audio_file)
            ai_response = ai.send_to_ai(user_input)
            ai_path = convert.geneate_ppt_audio(ai_response)
            # play.play_audio(ai_path)


    except KeyboardInterrupt:
        print("\nStopping...")



jarvis()  # Start the conversation



