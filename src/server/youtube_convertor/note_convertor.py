import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft
from scipy.io import wavfile # get the api
from operator import eq


class NoteConvertor(object):
    
    def __init__(self, wave):
        self.wave = wave.T[0]
        self.rate = 44000
        self.block_size = int(self.rate / 10)
        self.block_length = int(len(wave) / self.block_size)

    def convert(self):
        notes = []
        for i in range(0, self.block_length):
            part = self.wave[self.block_size * i: self.block_size * (i+1)]
            pitch = self.__fourier_transform(part)
            note = self.__decide_note(pitch)
            notes.append(note)
        return notes

    def __fourier_transform(self, wave_sample):
        size = len(wave_sample)
        k = np.arange(size)
        
        f0=k*self.rate/size    # double sides frequency range
        f0=f0[range(int(size/2))]
        
        Y=np.fft.fft(wave_sample)/size        # fft computing and normaliation
        Y=Y[range(int(size/2))]          # single sied frequency range
        
        amplitude_Hz = 2*abs(Y)
        phase_ang = np.angle(Y)*180/np.pi
        bank = np.where((amplitude_Hz >= (amplitude_Hz.max() * 0.75)) & (amplitude_Hz > 400))
        if len(bank[0]) > 1:
            return bank
        else:
            return -1

    def __decide_note(self, pitch):
        if pitch > 127 and pitch <= 131:
            return "C3"
        elif pitch > 131 and pitch <= 147:
            return "D3"
        elif pitch > 147 and pitch <= 165:
            return "E3"
        elif pitch > 165 and pitch <= 175:
            return "F3"
        elif pitch > 175 and pitch <= 196:
            return "G3"
        elif pitch > 196 and pitch <= 220:
            return "A3"
        elif pitch > 220 and pitch <= 247:
            return "B3"
        elif pitch > 247 and pitch <= 262:
            return "C4"
        elif pitch > 262 and pitch <= 294:
            return "D4"
        elif pitch > 294 and pitch <= 330:
            return "E4"
        elif pitch > 330 and pitch <= 349:
            return "F4"
        elif pitch > 349 and pitch <= 392:
            return "G4"
        elif pitch > 392 and pitch <= 440:
            return "A4"
        elif pitch > 440 and pitch <= 494:
            return "B4"
        elif pitch > 494 and pitch <= 523:
            return "C5"
        elif pitch > 523 and pitch <= 587:
            return "D5"
        elif pitch > 587 and pitch <= 659:
            return "E5"
        elif pitch > 659 and pitch <= 698:
            return "F5"
        elif pitch > 698 and pitch <= 784:
            return "G5"
        elif pitch > 784 and pitch <= 880:
            return "A5"
        elif pitch > 880 and pitch <= 988:
            return "B5"
        elif pitch > 988 and pitch <= 1047:
            return "C6"
        elif pitch > 1047 and pitch <= 1175:
            return "D6"
        elif pitch > 1175 and pitch <= 1319:
            return "E6"
        elif pitch > 1319 and pitch <= 1397:
            return "F6"
        elif pitch > 1397 and pitch <= 1568:
            return "G6"
        elif pitch > 1568 and pitch <= 1760:
            return "A6"
        elif pitch > 1760 and pitch <= 1976:
            return "B6"
        else:
            return "_"


