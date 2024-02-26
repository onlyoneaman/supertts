from openai import OpenAI

def speak(text):
    client = OpenAI()
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
