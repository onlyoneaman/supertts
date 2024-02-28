
def save_audio(response, filename):
    """
    Saves the audio response to a file.

    :param response: The audio response from tts.tts().
    :param filename: The filename to save the audio to.
    """
    if isinstance(response, bytes):
        audio_data = response
    # Check if the response is from OpenAI and needs additional handling
    elif hasattr(response, 'read'):
        # This assumes the response object has a read() method to get bytes
        audio_data = response.read()
    else:
        raise TypeError("Unsupported response type for saving audio.")

    with open(filename, 'wb') as f:
        f.write(audio_data)