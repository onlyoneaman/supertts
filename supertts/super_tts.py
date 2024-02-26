from supertts.providers import openai_provider, google_provider, azure_provider

class SuperTTS:
    def __init__(self, provider='openai'):
        self.provider = provider

    def tts(self, text, provider=None, voice=None, model=None):
        """
        Converts text to speech using the specified voice and model.

        :param text: The text to convert to speech.
        :param voice: The voice to use for the TTS.
        :param model: The TTS model to use.
        :return: An audio stream or file.
        """
        provider = provider or self.provider
        if provider == 'openai':
            return openai_provider.tts(text, voice=voice, model=model)
        elif provider == 'google':
            return google_provider.tts(text)
        elif provider == 'azure':
            return azure_provider.tts(text)
        else:
            raise ValueError(f"Unsupported provider: {provider}")

    def voices(self, provider=None):
        """
        Lists available voices for the current TTS provider.

        :return: A list of available voices.
        """
        provider = provider or self.provider
        if provider == 'openai':
            return openai_provider.available_voices()
        elif provider == 'google':
            return google_provider.available_voices()
        elif provider == 'azure':
            return azure_provider.available_voices()
        else:
            raise ValueError(f"Unsupported provider: {provider}")
