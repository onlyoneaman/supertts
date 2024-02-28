from supertts.providers import google_provider
from supertts.providers.azure_provider import AzureProvider
from supertts.providers.openai_provider import OpenAIProvider
from supertts.constants import PROVIDERS

class SuperTTS:
    def __init__(self, provider='openai'):
        self.provider = provider
        self.openai = OpenAIProvider()
        self.azure = AzureProvider()

    def tts(
        self, 
        text, 
        provider=None, 
        voice=None, 
        model=None
    ):
        """
        Converts text to speech using the specified voice and model.

        :param text: The text to convert to speech.
        :param provider: The TTS provider to use. (openai, google, azure)
        :param voice: The voice to use for the TTS.
        :param model: The TTS model to use.
        :return: An audio stream or file.
        """
        provider = provider or self.provider
        if provider == PROVIDERS["openai"]:
            return self.openai.synthesis(text, voice=voice, model=model)
        elif provider == PROVIDERS["google"]:
            return google_provider.synthesis(text)
        elif provider == PROVIDERS["azure"]:
            return self.azure.synthesis(text)
        else:
            raise ValueError(f"Unsupported provider: {provider}")

    def voices(self, provider=None):
        """
        Lists available voices for the current TTS provider.

        :param provider: The TTS provider to use. (openai, google, azure)
        :return: A list of available voices.
        """
        provider = provider or self.provider
        if provider == PROVIDERS["openai"]:
            tts = self.openai
        elif provider == PROVIDERS["google"]:
            return google_provider.available_voices()
        elif provider == PROVIDERS["azure"]:
            tts = self.azure
        else:
            raise ValueError(f"Unsupported provider: {provider}")
        return tts.available_voices()
