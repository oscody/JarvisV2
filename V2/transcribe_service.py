import speech_recognition as sr
import time
import play_service as play
import pyaudio
import wave
import math
import struct
import simpleaudio as sa
import os
from faster_whisper import WhisperModel

class transcribe:
    def __init__(self):
        # Audio parameters
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 1
        self.RATE = 44100
        self.CHUNK = 1024
        self.THRESHOLD = 1000  # Silence threshold
        self.SILENCE_DURATION = 1  # Seconds of silence to signify end of command

        # Get the directory of the current script
        self.script_dir = os.path.dirname(os.path.abspath(__file__))

        # Get the parent directory
        parent_dir = os.path.dirname(self.script_dir)

        self.file_path = os.path.join(parent_dir, "voice_recording/")
        print("file_path", self.file_path)
        self.file_name = "Jarvis_recordingV2.wav"
        self.file_path = os.path.join(self.file_path, self.file_name)
        print(f"file_path-{self.file_path}")

        self.siren = "sound_effects/puru_introv3.wav"

        # Initialize recognizer
        self.r = sr.Recognizer()

        # Initialize the Whisper model
        self.model_size = "small.en"
        self.whisper_model = WhisperModel(self.model_size, compute_type="int8")

    def record_until_pause(self):
        """Record audio from the microphone until a pause is detected."""
        print("Listening... Speak now.")
        play.play_audio(self.siren)
        audio = pyaudio.PyAudio()
        stream = audio.open(format=self.FORMAT, channels=self.CHANNELS,
                            rate=self.RATE, input=True,
                            frames_per_buffer=self.CHUNK)

        frames = []
        silent_chunks = 0
        silent_chunks_threshold = int(self.SILENCE_DURATION * self.RATE / self.CHUNK)
        started = False

        while True:
            data = stream.read(self.CHUNK, exception_on_overflow=False)
            is_silence = self._is_silent(data)

            if not started:
                if not is_silence:
                    started = True
                    frames.append(data)
            else:
                frames.append(data)
                if is_silence:
                    silent_chunks += 1
                else:
                    silent_chunks = 0

                if silent_chunks > silent_chunks_threshold:
                    break

        stream.stop_stream()
        stream.close()
        audio.terminate()

        if not frames:
            print("No speech detected.")
            return None

        with wave.open(self.file_path, 'wb') as wave_file:
            wave_file.setnchannels(self.CHANNELS)
            wave_file.setsampwidth(audio.get_sample_size(self.FORMAT))
            wave_file.setframerate(self.RATE)
            wave_file.writeframes(b''.join(frames))

        return self.file_path

    def _is_silent(self, data_chunk):
        """Check if the given audio chunk is silent."""
        rms = math.sqrt(sum(
            sample ** 2 for sample in struct.unpack("<" + "h" * (len(data_chunk) // 2), data_chunk)
        ) / len(data_chunk))
        return rms < self.THRESHOLD

    def transcribe_with_whisper(self, audio_file):
        print(f"Transcribing with Whisper model")
        segments, info = self.whisper_model.transcribe(audio_file, beam_size=5)
        transcription = ""
        for segment in segments:
            transcription += segment.text + " "
        print(transcription)
        return transcription.strip()

    def custom_transcribe_whisper(self):
        audio_path = self.record_until_pause()
        if audio_path:
            text = self.transcribe_with_whisper(audio_path)
            print(f"Done path {audio_path}")
            return text
        else:
            return ""

    def speech_recognition_whisper(self):
        start_time = time.time()
        with sr.Microphone() as source:
            self.r.adjust_for_ambient_noise(source)
            play.play_audio(self.siren)
            print("Say something!")
            try:
                audio = self.r.listen(source, timeout=10, phrase_time_limit=15)
                print("Found audio")
                text = self.r.recognize_whisper(audio)
                print("You said: " + text)
                end_time = time.time()
                print(f"Recording finished. Duration: {end_time - start_time} seconds.")
                return text
            except sr.UnknownValueError:
                print("Speech Recognition could not understand audio")
            except sr.RequestError as e:
                print(f"Could not request results; {e}")
            except sr.WaitTimeoutError:
                print("Listening timed out while waiting for phrase to start")
                return ""
