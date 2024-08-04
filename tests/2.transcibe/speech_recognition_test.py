import speech_recognition as sr
import time


r = sr.Recognizer()

start_time = time.time()

with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source,5,3)
    try:

        # Use Google's speech recognition to convert the audio to text
        text = r.recognize_google(audio)
        print("You said: " + text)

        end_time = time.time()
        print(f"Recording finished. Duration: {end_time - start_time} seconds.")

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))