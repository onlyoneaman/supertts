import unittest
from supertts import SuperTTS

class TestCoreFunctionality(unittest.TestCase):
    def test_tts_without_provider(self):
        """Test that tts function raises ValueError when no provider is found."""
        supertts = SuperTTS()
        with self.assertRaises(ValueError):
            supertts.tts("Hello world", provider="nonexistent")

    def test_voices_without_provider(self):
        """Test that voices function raises ValueError when no provider is found."""
        supertts = SuperTTS()
        with self.assertRaises(ValueError):
            supertts.voices(provider="nonexistent")

if __name__ == '__main__':
    unittest.main()
