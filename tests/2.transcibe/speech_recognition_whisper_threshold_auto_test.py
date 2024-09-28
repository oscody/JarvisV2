# Not getting good results with it recording the audio on py
# Initial energy threshold: 322.8907883968555
# Current energy threshold: 322.8907883968555

# https://github.com/PromtEngineer/Verbi/blob/main/voice_assistant/audio.py

import speech_recognition as sr
import time
import whisper

r = sr.Recognizer()

# Set the total duration to listen for (in seconds)
total_listen_duration = 10
start_time = time.time()

with sr.Microphone() as source:
    # Adjust for ambient noise
    # r.adjust_for_ambient_noise(source, duration=0.5)
    print("Say something!")

    r.energy_threshold = 150
    r.pause_threshold = 1.0
    r.phrase_threshold = 0.3
    
    print(f"Initial energy threshold: {r.energy_threshold}")
    r.dynamic_energy_threshold = False

    # Continue listening until total_listen_duration has passed
    while time.time() - start_time < total_listen_duration:
        try:
            current_threshold = r.energy_threshold
            print(f"Current energy threshold: {current_threshold}")
            
            # Listen for speech with a timeout of 5 seconds
            audio = r.listen(source, timeout=5,phrase_time_limit=15,)
            print("found audio")

            # Process the audio with Whisper
            text = r.recognize_whisper(audio)
            print("You said: " + text)

            # Exit loop if speech is recognized before the total duration is reached
            # break

        except sr.UnknownValueError:
            print("Whisper could not understand the audio")
        except sr.RequestError as e:
            print(f"Could not request results from Whisper service; {e}")
        except sr.WaitTimeoutError:
            print("Listening timed out while waiting for phrase to start")
        # If the total duration is exceeded, the loop will exit automatically

end_time = time.time()
print(f"Recording finished. Total time: {end_time - start_time} seconds.")
