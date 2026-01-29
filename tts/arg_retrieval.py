import argparse
import os

from dotenv import load_dotenv
load_dotenv()

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_tts_arguments():
    parser = argparse.ArgumentParser(description="Argument Retrieval for TTS")
    parser.add_argument("--model_path", type=str, help="Path to the TTS model file", default=os.getenv("TTS_MODEL_PATH"))
    parser.add_argument("--config_path", type=str, help="Path to the TTS config file",default=os.getenv("TTS_CONFIG_PATH"))
    parser.add_argument("--audio_prompt", type=str, help="Path to the audio prompt for voice cloning", default=os.getenv("AUDIO_PROMPT_PATH"))
    parser.add_argument("--output_path", type=str, help="Path to save the generated audio file", default=os.getenv("OUTPUT_AUDIO_PATH"))
    parser.add_argument("--text", type=str, required=True, help="Text to be synthesized")
    args = parser.parse_args()
    logger.info(f"Model Name: {args.model_path.split('/')[-2] if args.model_path else 'Not Provided'}")
    return args