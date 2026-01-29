# Init TTS with the target model name
from TTS.api import TTS

from conversational_agent.tts.arg_retrieval import get_tts_arguments

# Load the TTS model from local path
args = get_tts_arguments()
tts = TTS(
            model_path=args.model_path,
            config_path=args.config_path,
        ).to("cuda")
tts.tts_to_file(args.text, speaker_wav=args.audio_prompt, language="en", file_path=args.output_path)
