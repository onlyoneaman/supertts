# This is a placeholder for the actual OpenAI API client import and setup
# Assume `openai_api_client` is a configured client for the OpenAI API

def speak(text):
    # Implement the function to send text to OpenAI's TTS service
    # and return the audio data
    pass

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
