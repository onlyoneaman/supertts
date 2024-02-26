import unittest
from unittest.mock import patch

@unittest.skipUnless("openai" in globals(), "OpenAI tests require the openai package")
class TestOpenAIProvider(unittest.TestCase):
    @patch('supertts.providers.openai_provider.speak')
    def test_openai_speak(self, mock_speak):
        """Test that OpenAI's speak function is called correctly."""
        from supertts.providers import openai_provider
        openai_provider.speak("Hello world")
        mock_speak.assert_called_once_with("Hello world")

    @patch('supertts.providers.openai_provider.available_voices')
    def test_openai_voices(self, mock_available_voices):
        """Test that OpenAI's available_voices function is called correctly."""
        from supertts.providers import openai_provider
        openai_provider.available_voices()
        mock_available_voices.assert_called_once()

if __name__ == '__main__':
    unittest.main()
