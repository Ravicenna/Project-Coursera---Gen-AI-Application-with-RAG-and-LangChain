import unittest
from EmotionDetection import emotion_detector

class TestEmotionDetector(unittest.TestCase):

    def test_emotions(self):
        result = emotion_detector("I am happy")

        self.assertIsNotNone(result)
        self.assertIn("joy", result)

if __name__ == "__main__":
    unittest.main()