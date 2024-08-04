
import speech_recognition as sr
import time
import whisper

def audio_text():

    r = sr.Recognizer()

    start_time = time.time()

    with sr.Microphone() as source:

        r.adjust_for_ambient_noise(source)
        print("Say something!")

        try:
            audio = r.listen(source,timeout=10)
            
            text = r.recognize_whisper(audio)
            print("You said: " + text)

            end_time = time.time()
            print(f"Recording finished. Duration: {end_time - start_time} seconds.")
            return text

        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
        except sr.WaitTimeoutError:
            print("Listening timed out while waiting for phrase to start")
            return ""