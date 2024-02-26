from openai import OpenAI
import os

def get_openai_api_key():
    """Retrieve the OPENAI_API_KEY environment variable."""
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        raise EnvironmentError('The environment variable OPENAI_API_KEY is not set. Please set it to your OpenAI API key.')
    return api_key

def speak(text):
    client = OpenAI(
        api_key=get_openai_api_key()
    )
    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
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
