import unittest
from supertts import tts, voices

class TestCoreFunctionality(unittest.TestCase):
    def test_tts_without_provider(self):
        """Test that tts function raises ValueError when no provider is found."""
        with self.assertRaises(ValueError):
            tts("Hello world", provider="nonexistent")

    def test_voices_without_provider(self):
        """Test that voices function raises ValueError when no provider is found."""
        with self.assertRaises(ValueError):
            voices(provider="nonexistent")

if __name__ == '__main__':
    unittest.main()
