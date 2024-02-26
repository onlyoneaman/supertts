from supertts.providers import openai_provider, google_provider, azure_provider

def tts(text, provider='openai'):
    if provider == 'openai':
        return openai_provider.speak(text)
    elif provider == 'google':
        return google_provider.speak(text)
    elif provider == 'azure':
        return azure_provider.speak(text)
    else:
        raise ValueError("Unsupported provider")

def voices(provider='openai'):
    if provider == 'openai':
        return openai_provider.available_voices()
    elif provider == 'google':
        return google_provider.available_voices()
    elif provider == 'azure':
        return azure_provider.available_voices()
    else:
        raise ValueError("Unsupported provider")
