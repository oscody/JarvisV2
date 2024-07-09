# Not wOrking

import os
import time
import torch
import torchaudio
from TTS.tts.configs.xtts_config import XttsConfig
from TTS.tts.models.xtts import Xtts
import soundfile as sf

audioPath = "Voice/Wolf.wav"
file_path = 'Voice/Concert.txt'


print("Loading model...")
config = XttsConfig()
config.load_json("./XTTS-v2/config.json")
model = Xtts.init_from_config(config)
model.load_checkpoint(config, checkpoint_dir="./XTTS-v2/")

# Check if CUDA is available and move the model to the appropriate device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

print("Computing speaker latents...")
gpt_cond_latent, speaker_embedding = model.get_conditioning_latents(audio_path=[audioPath])


def prepare_attention_mask(inputs, pad_token_id):
    if isinstance(inputs, torch.Tensor):
        if inputs.dim() == 2:
            inputs = inputs.view(-1)
        attention_mask = torch.isin(inputs, torch.tensor([pad_token_id], dtype=inputs.dtype, device=inputs.device)).logical_not()
        return attention_mask.to(dtype=torch.long)
    raise ValueError("Inputs should be a Tensor")

# Custom function to prepare attention mask
pad_token_id = 0  # Replace with the actual pad_token_id if different
attention_mask = prepare_attention_mask(gpt_cond_latent, pad_token_id)

print("Prepared attention mask for generation...")

print("Inference...")
t0 = time.time()
try:
    chunks = model.inference_stream(
        "It took me quite a long time to develop a voice and now that I have it I am not going to be silent.",
        "en",
        gpt_cond_latent,
        speaker_embedding
    )
except TypeError as e:
    print(f"gpt_cond_latent type: {type(gpt_cond_latent)}")
    print(f"gpt_cond_latent: {gpt_cond_latent}")
    print(f"speaker_embedding type: {type(speaker_embedding)}")
    print(f"speaker_embedding: {speaker_embedding}")
    raise

wav_chunks = []
for i, chunk in enumerate(chunks):
    if i == 0:
        print(f"Time to first chunk: {time.time() - t0}")
    print(f"Received chunk {i} of audio length {chunk.shape[-1]}")
    wav_chunks.append(chunk)

wav = torch.cat(wav_chunks, dim=0)
torchaudio.save("xtts_streaming.wav", wav.squeeze().unsqueeze(0).cpu(), 24000)
