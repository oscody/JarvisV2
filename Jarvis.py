import sys
import os

# Ensure the helper directory is in the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'helper')))

import speech_to_text_service as transcribe
import play_service as play
import record_service as rec
import ai_service as ai
import text_to_speech_service as convert
from detect_platform import detect

platform = detect()
print(f"Platform detected: {platform}")

voicefolder = "voice_recording"
audio_file = os.path.join(voicefolder, "temp_recording.wav")

def jarvis():
    try:
        while True:
            rec_audio = rec.record_audio(5)

            if platform == "Mac":
                user_input = transcribe.transcribe_with_whisper_Mac(rec_audio)
                ai_response = ai.send_to_ai_mac(user_input)
                ai_path = convert.geneate_audio_tts(ai_response)
                play.play_audio(ai_path)

            elif platform == "Pi":
                user_input = transcribe.transcribe_with_whisper_Pi(rec_audio)
                ai_response = ai.send_to_ai_pi(user_input)
                ai_path = convert.geneate_ppt_audio(ai_response)

            
    except KeyboardInterrupt:
        print("\nStopping...")

jarvis()  # Start the conversation
