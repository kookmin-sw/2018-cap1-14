from youtube_convertor import WaveConvertor
import unittest
import math

class TestWaveConvertor(unittest.TestCase):

    def test_get_wave(self):
        rate, data = WaveConvertor().get_wave("https://www.youtube.com/watch?v=OxgiiyLp5pk")
        play_time = len(data) / rate
        self.assertEqual(44100, rate)
        self.assertEqual(339, math.floor(play_time))
