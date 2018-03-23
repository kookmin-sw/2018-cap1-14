from youtube_convertor import WaveConvertor
from youtube_convertor import Wave
import unittest

class TestWaveConvertor(unittest.TestCase):

    def test_get_wave(self):
        wave = WaveConvertor().get_wave("https://www.youtube.com/watch?v=OxgiiyLp5pk")
        print(wave)
        self.assertEqual(44100, wave.rate)
        self.assertEqual(339, wave.play_time)
        wave.fourier_transform()
        
