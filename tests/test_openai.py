import unittest
from unittest.mock import patch
import supertts
from supertts.providers import openai_provider

class TestOpenAIProvider(unittest.TestCase):
    @patch('supertts.providers.openai_provider.speak')
    def test_openai_speak(self, mock_speak):
        """Test that OpenAI's speak function is called correctly."""
        res=openai_provider.speak("Hello world", model="tts-1", voice="nova")
        res.stream_to_file("artifacts/hello_world.mp3")
        mock_speak.assert_called_once_with("Hello world", model="tts-1", voice="nova")

    def test_openai_voices(self):
        """Test that OpenAI's available_voices function is called correctly."""
        voices = openai_provider.available_voices()
        expected_voices = [
            {"name": "echo", "gender": "male"},
            {"name": "alloy", "gender": "male"},
            {"name": "fable", "gender": "male"},
            {"name": "onyx", "gender": "male"},
            {"name": "nova", "gender": "female"},
            {"name": "shimmer", "gender": "male"},
        ]

        voices_tuples = [tuple(voice.items()) for voice in voices]
        expected_voices_tuples = [tuple(voice.items()) for voice in expected_voices]

        self.assertEqual(set(voices_tuples), set(expected_voices_tuples), "Available voices do not match expected")

if __name__ == '__main__':
    unittest.main()
