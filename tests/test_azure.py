import unittest
from unittest.mock import patch
import os
from supertts import SuperTTS

class TestOpenAIProvider(unittest.TestCase):
    # @patch('supertts.providers.openai_provider.speak')
    # def test_azure_speak(self, mock_speak):
    #     """Test that OpenAI's speak function is called correctly."""
    #     res=openai_provider.speak("Hello world", model="tts-1", voice="nova")
    #     mock_speak.assert_called_once_with("Hello world", model="tts-1", voice="nova")

    @unittest.skipIf(os.getenv('AZURE_KEY') is None, "Azure key not set.")
    def test_azure_voices(self):
        """Test that Azure available_voices function is called correctly."""
        supertts = SuperTTS(provider="azure")
        voices = supertts.voices()

        # check if voices length is more than 0
        self.assertGreater(len(voices), 0, "No voices returned")

if __name__ == '__main__':
    unittest.main()
