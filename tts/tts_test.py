# Init TTS with the target model name
from TTS.api import TTS
import torch

# Get device
device = "cuda" if torch.cuda.is_available() else "cpu"

tts = TTS(model_name="tts_models/multilingual/multi-dataset/your_tts", progress_bar=True).to(device)
tts.tts_to_file("This is voice cloning test and it seems pretty fast.", speaker_wav="./test_prompt.wav", language="en", file_path="output.wav")
