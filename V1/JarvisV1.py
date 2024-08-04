import sys
import os

# Determine the root directory (two levels up from the current file's directory)
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Ensure the root directory is in the Python path
sys.path.insert(0, root_dir)

# Import modules from the root directory
import speech_to_text_service as transcribe
import play_service as play
import record_service as rec
import ai_service as ai
import text_to_speech_service as convert

# Import other modules
from helper.detect_platform import detect
import V1.JarvisV1_1transcription as listen

platform = detect()
print(f"Platform detected: {platform}")


def jarvis():
    try:
        while True:
            if platform == "Mac":
                user_input = listen.audio_text()
                if user_input:
                    print("User input:", user_input.lower())
                    
                       # Strip any leading/trailing whitespace and remove any punctuation
                    cleaned_input = user_input.lower().strip().replace(".", "").replace("!", "")
                    
                    # Check if the cleaned input is in the list of exit commands
                    if cleaned_input in ["terminate", "exit", "quit", "stop"]:
                        print("Exiting...")
                        break  # Exit the loop and stop execution

                    ai_response = ai.send_to_ai_mac(user_input)
                    ai_path = convert.geneate_speechify_audio(ai_response)
                else:
                    print("No input detected, restarting listening...")

            elif platform == "Pi":
                user_input = transcribe.transcribe_with_whisper_Pi()
                if user_input:
                    if user_input.lower().strip() == "terminate":
                        print("Exiting...")
                        break  # Exit the loop and stop execution

                    ai_response = ai.send_to_ai_pi(user_input)
                    ai_path = convert.geneate_ppt_audio(ai_response)
                else:
                    print("No input detected, restarting listening...")

    except KeyboardInterrupt:
        print("\nStopping...")

    finally:
        print("Jarvis has stopped. Goodbye!")

jarvis()  # Start the conversation
