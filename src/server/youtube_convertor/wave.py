import numpy
import math
import matplotlib.pyplot as plt

class Wave(object):
    
    def __init__(self, rate, data):
        self.rate = rate
        self.channel1 = data[:, 0]
        self.channel2 = data[:, 1]
        self.play_time = math.floor(len(data) / rate)
    
    def fourier_transform(self):
        result = numpy.fft.fft(self.channel1)
        return result
        
    def __repr__(self):
        return ('< rate = ' + str(self.rate) +
               ' play time = ' + str(math.floor(self.play_time / 60)) + ":" + str(self.play_time % 60) + ' >')
            
