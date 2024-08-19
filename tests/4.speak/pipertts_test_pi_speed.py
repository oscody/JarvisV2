import wave
import sounddevice as sd
import soundfile as sf
import numpy as np
import time
import simpleaudio as sa
from piper.voice import PiperVoice

# Setup
voicedir = "pipertts/"  # Directory where the ONNX model files are stored
model = voicedir + "en_US-norman-medium.onnx"
config = voicedir + "en_en_US_norman_medium_en_US-norman-medium.onnx.json"  # Correct config file name

# Load the model and config
voice = PiperVoice.load(model, config)

text_to_speak = "This is an example of text-to-speech saying 'Where onnx model files are stored on my machine'"

# Test using wave (writing to file)
start_wave = time.time()

# wav_file = wave.open("Voice/pipertts.wav", "w")
# audio = voice.synthesize(text_to_speak, wav_file)

with wave.open("Voice/pipertts.wav", "wb") as wav_file:
    wav_file.setnchannels(1)  # Mono
    wav_file.setsampwidth(2)  # 2 bytes per sample (16 bits)
    wav_file.setframerate(voice.config.sample_rate)  # Sample rate
    
    
    audio = voice.synthesize(text_to_speak,wav_file)


    # wav_file.writeframes(audio)

end_wave = time.time()
wave_time = end_wave - start_wave
print(f"Time taken to synthesize and write to file: {wave_time:.4f} seconds")



# Playback using simpleaudio
start_sa = time.time()
wave_obj = sa.WaveObject.from_wave_file("Voice/pipertts.wav")
play_obj = wave_obj.play()
play_obj.wait_done()  # Wait until sound has finished playing
end_sa = time.time()
sa_time = end_sa - start_sa
print(f"Time taken to play back using simpleaudio: {sa_time:.4f} seconds")

# Playback using sounddevice (from wav file)
start_sd = time.time()

# Use soundfile to read the .wav file
data, samplerate = sf.read('Voice/pipertts.wav', dtype='int16')

# Play the audio data using sounddevice
sd.play(data, samplerate)
sd.wait()  # Wait until file is done playing

end_sd = time.time()
sd_time = end_sd - start_sd
print(f"Time taken to play back using sounddevice (from file): {sd_time:.4f} seconds")

# Test using sounddevice (streaming playback directly from synthesis)
start_sd_stream = time.time()

# Setup a sounddevice OutputStream with appropriate parameters
stream = sd.OutputStream(samplerate=voice.config.sample_rate, channels=1, dtype='int16')
stream.start()

for audio_bytes in voice.synthesize_stream_raw(text_to_speak):
    int_data = np.frombuffer(audio_bytes, dtype=np.int16)
    stream.write(int_data)

stream.stop()
stream.close()

end_sd_stream = time.time()
sd_stream_time = end_sd_stream - start_sd_stream
print(f"Time taken to synthesize and stream audio using sounddevice: {sd_stream_time:.4f} seconds")

# Print out the results for comparison
print(f"\nTime to synthesize and write to file: {wave_time:.4f} seconds")
print(f"Simpleaudio playback time: {sa_time:.4f} seconds")
print(f"Sounddevice playback time (from file): {sd_time:.4f} seconds")
print(f"Sounddevice synthesize and stream time: {sd_stream_time:.4f} seconds")
