import azure.cognitiveservices.speech as speechsdk
import os

class AzureProvider:
    def __init__(
        self, 
        subscription_key=os.getenv("AZURE_KEY"), 
        region=os.getenv("AZURE_REGION")
    ):
        if not subscription_key:
            raise ValueError("Azure subscription key not provided. Set the AZURE_KEY environment variable.")
        if not region:
            raise ValueError("Azure region not provided. Set the AZURE_REGION environment variable.")
        self.subscription_key = subscription_key
        self.region = region

    def synthesis(
        self, 
        text,
        voice_name=None,
        language="en-US"
    ):
        speech_config = speechsdk.SpeechConfig(
            subscription=self.subscription_key, 
            region=self.region
        )
        speech_config.speech_synthesis_language = language
        if voice_name is not None:
            speech_config.speech_synthesis_voice_name = voice_name
        
        audio_config = None

        speech_synthesizer = speechsdk.SpeechSynthesizer(
            speech_config=speech_config,
            audio_config=audio_config
        )

        result = speech_synthesizer.speak_text_async(text).get()

        if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
            return result.audio_data
        elif result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = result.cancellation_details
            print(f"Speech synthesis canceled: {cancellation_details.reason}")
            if cancellation_details.reason == speechsdk.CancellationReason.Error:
                print(f"Error details: {cancellation_details.error_details}")
                raise ValueError(f"Error details: {cancellation_details.error_details}")
            raise ValueError(f"Speech synthesis canceled: {cancellation_details.reason}")

    def available_voices(self):
        voices = []
        speech_config = speechsdk.SpeechConfig(
            subscription=self.subscription_key, 
            region=self.region
        )

        speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)

        result = speech_synthesizer.get_voices_async().get()

        if result.reason == speechsdk.ResultReason.VoicesListRetrieved:
            for voice in result.voices:
                voice_object = {
                    'name': voice.name,
                    'locale': voice.locale,
                    'gender': voice.gender,
                    'localName': voice.local_name,
                }
                voices.append(voice_object)
            return voices
        elif result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = result.cancellation_details
            print(f"Speech synthesis canceled: {cancellation_details.reason}")
            if cancellation_details.reason == speechsdk.CancellationReason.Error:
                print(f"Error details: {cancellation_details.error_details}")
                raise ValueError(f"Error details: {cancellation_details.error_details}")
            raise ValueError(f"Speech synthesis canceled: {cancellation_details.reason}")        
