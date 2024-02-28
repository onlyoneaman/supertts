from openai import OpenAI
import os

DEFAULT_MODEL = "tts-1"
DEFAULT_VOICE = "alloy"

VOICES = [
            {
                "name": "alloy",
                "gender": "male"
            },
            {
                "name": "echo",
                "gender": "male"
            },
            {
                "name": "fable",
                "gender": "male"
            },
            {
                "name": "onyx",
                "gender": "male"
            },
            {
                "name": "nova",
                "gender": "female"
            },
            {
                "name": "shimmer",
                "gender": "male"
            },
        ]

class OpenAIProvider:
    def __init__(self):
        self.client = OpenAI(
            api_key=self.get_openai_api_key()
        )
        self.voices = VOICES

    def get_openai_api_key(self):
        """Retrieve the OPENAI_API_KEY environment variable."""
        api_key = os.getenv('OPENAI_API_KEY')
        if not api_key:
            raise EnvironmentError('The environment variable OPENAI_API_KEY is not set. Please set it to your OpenAI API key.')
        return api_key

    def synthesis(
        self,
        text,
        model: str = DEFAULT_MODEL,
        voice: str = DEFAULT_VOICE
    ):
        model = DEFAULT_MODEL if model is None else model
        voice = DEFAULT_VOICE if voice is None else voice
        voices = self.available_voices()
        if model not in ["tts-1", "tts-1-hd"]:
            raise ValueError(f"Invalid model: {model}")
        if voice not in [voice["name"] for voice in voices]:
            raise ValueError(f"Invalid voice: {voice}")
        response = self.client.audio.speech.create(
            model=model,
            voice=voice,
            input=text
        )
        return response
    
    def available_voices(
        self
    ):
        return self.voices
