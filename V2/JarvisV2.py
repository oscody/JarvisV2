import sys
import os

# Determine the root directory (two levels up from the current file's directory)
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Ensure the root directory is in the Python path
sys.path.insert(0, root_dir)

# Import modules from the root directory
from V2.transcribe_service import transcribe
import play_service as play
import record_service as rec
# import ai_service as ai
# from V2.ai_serviceV2 import Ollama
from V2.ai_serviceV3 import llm
import text_to_speech_service as convert

# Import other modules
from helper.detect_platform import detect
import V2.JarvisV1_1transcription as listen
import helper.detect_wakeword as wake

print(f"V2")

platform = detect()
print(f"Platform detected: {platform}")



def jarvis():
    try:
        # Create an instance
        transcriber = transcribe()
        ai_model = llm()
        while True:
            
            # Outer loop: Wait for the wake word
            if wake.detection_wake_word(platform):

                print("Wake word detected. Listening for user input...")

                # Inner loop: Try to get audio input twice
                count = 0

                while count < 2:
                    
                    if platform == "Mac":
                        user_input = transcriber.speech_recognition_whisper()
                    elif platform == "Pi":
                        user_input = transcriber.custom_transcribe_whisper()
                    else:
                        print("Unsupported platform.")
                        return
                    
                    if user_input:

                        # Strip any leading/trailing whitespace and remove any punctuation

                        user_input = user_input.lower().strip().replace(".", "").replace("!", "")
                        print("User input:", user_input)



                        # Check if the cleaned input is in the list of exit commands
                        if user_input in ["terminate", "exit", "quit", "stop"]:
                            print("Exiting...")
                            return  # Exit the function to stop execution

                        elif user_input in ["thank you"]:
                            print("Restarting listening...")
                            count += 1
                            break  # Break the inner loop and listen for the wake word again

                        # Process the user input with AI service
                        # ai_response = ai.send_to_ai_mac(user_input) if platform == "Mac" else ai.send_to_ai_pi(user_input)
                        ai_response = ai_model.invoke(user_input,session_id="1", language="english")
                        ai_path = convert.geneate_speechify_audio(ai_response) if platform == "Mac" else convert.geneate_ppt_audio(ai_response)
                        # break  # Break the inner loop as we received valid input
                    
                    else:
                        print("No input detected. Attempting again...")
                        count += 1

                # If no valid input is detected in two attempts, restart listening for the wake word
                if count == 2:
                    print("No valid input after two attempts. Returning to wake word detection...")

    except KeyboardInterrupt:
        print("\nStopping...")

    finally:
        print("Jarvis has stopped. Goodbye!")

jarvis()  # Start the conversation
