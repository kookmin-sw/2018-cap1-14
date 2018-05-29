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
            pitchs = self.__fourier_transform(part)
            note = []
            for pitch in pitchs:
              note.append(self.__decide_note(pitch))
            notes.append(note)

	    #remove junk

	    for i in range(1, len(notes)):
	      if (notes[i]["pitch"] == "_" and notes[i]["pitch"] != notes[i-1]["pitch"] and notes[i]["pitch"] != notes[i+1]["pitch"]):
	        notes[i]["pitch"] = notes[i-1]["pitch"]
		notes[i]["octave"] = notes[i-1]["octave"]
		
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
        banks = np.where((amplitude_Hz >= (amplitude_Hz.max() * 0.90)) & (amplitude_Hz > 500))
        pitchs = []
        for bank in banks[0]:
          pitchs.append(f0[bank])
        return pitchs

    def __decide_note(self, pitch):
        if pitch > 127 and pitch <= 134:
            return {"pitch":1, "octave" : 3}
        elif pitch > 131 and pitch <= 147:
            return {"pitch":2, "octave" : 3}
        elif pitch > 147 and pitch <= 165:
            return {"pitch":3, "octave" : 3}
        elif pitch > 165 and pitch <= 175:
            return {"pitch":4, "octave" : 3}
        elif pitch > 175 and pitch <= 196:
            return {"pitch":5, "octave" : 3}
        elif pitch > 196 and pitch <= 220:
            return {"pitch":6, "octave" : 4}
        elif pitch > 220 and pitch <= 247:
            return {"pitch":7, "octave" : 4}
        elif pitch > 247 and pitch <= 262:
            return {"pitch":1, "octave" : 4}
        elif pitch > 262 and pitch <= 294:
            return {"pitch":2, "octave" : 4}
        elif pitch > 294 and pitch <= 330:
            return {"pitch":3, "octave" : 4}
        elif pitch > 330 and pitch <= 349:
            return {"pitch":4, "octave" : 4}
        elif pitch > 349 and pitch <= 392:
            return {"pitch":5, "octave" : 4}
        elif pitch > 392 and pitch <= 440:
            return {"pitch":6, "octave" : 5}
        elif pitch > 440 and pitch <= 494:
            return {"pitch":7, "octave" : 5}
        elif pitch > 494 and pitch <= 523:
            return {"pitch":1, "octave" : 5}
        elif pitch > 523 and pitch <= 587:
            return {"pitch":2, "octave" : 5}
        elif pitch > 587 and pitch <= 659:
            return {"pitch":3, "octave" : 5}
        elif pitch > 659 and pitch <= 698:
            return {"pitch":4, "octave" : 5}
        elif pitch > 698 and pitch <= 784:
            return {"pitch":5, "octave" : 5}
        elif pitch > 784 and pitch <= 880:
            return {"pitch":6, "octave" : 6}
        elif pitch > 880 and pitch <= 988:
            return {"pitch":7, "octave" : 6}
        elif pitch > 988 and pitch <= 1047:
            return {"pitch":1, "octave" : 6}
        elif pitch > 1047 and pitch <= 1175:
            return {"pitch":2, "octave" : 6}
        elif pitch > 1175 and pitch <= 1319:
            return {"pitch":3, "octave" : 6}
        elif pitch > 1319 and pitch <= 1397:
            return {"pitch":4, "octave" : 6}
        elif pitch > 1397 and pitch <= 1568:
            return {"pitch":5, "octave" : 6}
        elif pitch > 1568 and pitch <= 1760:
            return {"pitch":6, "octave" : 7}
        elif pitch > 1760 and pitch <= 1976:
            return {"pitch":7, "octave" : 7}
        else:
            return {"pitch":"_"}

