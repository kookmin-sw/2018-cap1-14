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
        return self.__test_remove_duplication(self.__filter(notes))

    def __fourier_transform(self, wave_sample):
        size = len(wave_sample)
        k = np.arange(size)
        
        f0=k*self.rate/size    # double sides frequency range
        f0=f0[range(int(size/2))]
        
        Y=np.fft.fft(wave_sample)/size        # fft computing and normaliation
        Y=Y[range(int(size/2))]          # single sied frequency range
        
        amplitude_Hz = 2*abs(Y)
        phase_ang = np.angle(Y)*180/np.pi
        bank = np.where((amplitude_Hz >= (amplitude_Hz.max() / 4)) & (amplitude_Hz > 400))
        if len(bank[0]) > 1:
            return f0[bank[0][0]]
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
        else:
            return "_"

    def __filter(self, notes):
        note = notes[0]
        equal_counter = 0

        for i in range(1, self.block_length):
            if notes[i] == note:
                equal_counter += 1
            else:
                if equal_counter < 1:
                    notes[i - 1] = note
                equal_counter = 0
            
            notes[i - 1] = notes[i - 1]
        return notes

    def __test_remove_duplication(self, notes):
        temp = notes[0]
        result = []
        for note in notes:
            if temp != note:
                result.append(temp)
                temp = note
        return result           
        

