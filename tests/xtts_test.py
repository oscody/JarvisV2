
import torch
from TTS.tts.configs.xtts_config import XttsConfig
from TTS.tts.models.xtts import Xtts
import soundfile as sf

audioPath = "Voice/Wolf.wav"

file_path = 'Voice/Concert.txt'

# Open the file in read mode
with open(file_path, 'r') as file:
    # Read the contents of the file
    file_contents = file.read()


text_to_speak = file_contents

config = XttsConfig()
config.load_json("./XTTS-v2/config.json")
model = Xtts.init_from_config(config)
model.load_checkpoint(config, checkpoint_dir="./XTTS-v2/")

# Check if CUDA is available and move the model to the appropriate device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)



 # Use XTTS to synthesize speech
outputs = model.synthesize(
    text_to_speak,  # Pass the prompt as a string directly
    config,
    speaker_wav=audioPath,  # Pass the file path directly
    gpt_cond_len=24,
    temperature=0.5,
    language='en',
    speed=1.4  # Specify the desired language
)

#Get the synthesized audio tensor from the dictionary
synthesized_audio = outputs['wav']


output_file_path = './outputs/output_audio.wav'
sample_rate = config.audio.sample_rate
sf.write(output_file_path, synthesized_audio, sample_rate)