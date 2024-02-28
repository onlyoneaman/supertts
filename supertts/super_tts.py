from supertts.providers.azure_provider import AzureProvider
from supertts.providers.openai_provider import OpenAIProvider
from supertts.providers.google_provider import GoogleProvider
from supertts.constants import PROVIDERS

class SuperTTS:
    def __init__(self, provider='openai'):
        self.provider = provider
        self.openai = OpenAIProvider()
        self.azure = AzureProvider()
        self.google = GoogleProvider()

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
        if provider == PROVIDERS["OPENAI"]:
            return self.openai.synthesis(text, voice=voice, model=model)
        elif provider == PROVIDERS["GOOGLE"]:
            return self.google.synthesis(text)
        elif provider == PROVIDERS["AZURE"]:
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
        if provider == PROVIDERS["OPENAI"]:
            tts = self.openai
        elif provider == PROVIDERS["GOOGLE"]:
            tts = self.google
        elif provider == PROVIDERS["AZURE"]:
            tts = self.azure
        else:
            raise ValueError(f"Unsupported provider: {provider}")
        return tts.available_voices()
