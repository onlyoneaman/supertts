from openai import OpenAI
import os

def get_openai_api_key():
    """Retrieve the OPENAI_API_KEY environment variable."""
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        raise EnvironmentError('The environment variable OPENAI_API_KEY is not set. Please set it to your OpenAI API key.')
    return api_key

def speak(
    text,
    model: str = "tts-1",
    voice: str = "alloy"
):
    voices = available_voices()
    if model not in ["tts-1", "tts-1-hd"]:
        raise ValueError(f"Invalid model: {model}")
    if voice not in [voice["name"] for voice in voices]:
        raise ValueError(f"Invalid voice: {voice}")
    client = OpenAI(
        api_key=get_openai_api_key()
    )
    response = client.audio.speech.create(
        model=model,
        voice=voice,
        input=text
    )
    return response

def available_voices():
    voices = [
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
    return voices
