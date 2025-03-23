from EmotionDetection import emotion_detector
import unittest

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):
        joy_sut = emotion_detector("I am glad this happened")
        self.assertEqual(joy_sut["dominant_emotion"],"joy")

        anger_sut = emotion_detector("I am really mad about this")
        self.assertEqual(anger_sut["dominant_emotion"],"anger")

        disgust_sut = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(disgust_sut["dominant_emotion"],"disgust")

        sadness_sut = emotion_detector("I am so sad about this")
        self.assertEqual(sadness_sut["dominant_emotion"],"sadness")

        fear_sut = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(fear_sut["dominant_emotion"],"fear")

unittest.main()        