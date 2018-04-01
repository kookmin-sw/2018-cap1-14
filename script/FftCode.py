import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft
from scipy.io import wavfile # get the api

fs, data = wavfile.read('Air.wav') # load the data
y = data.T[0] # this is a two channel soundtrack, I get the first track
time = data.shape[0] / rate


blockSize = int(fs / 10)
blockHall = int(len(y) / blockSize)

for i in range(0, blockHall):
    part = y[blockSize * i: blockSize * (i+1)]
    n=len(part)        # Length of signal
    NFFT=n      # ?? NFFT=2^nextpow2(length(y))  ??
    k=np.arange(NFFT)
    f0=k*fs/NFFT    # double sides frequency range
    f0=f0[range(int(NFFT/2))]

    Y=np.fft.fft(part)/NFFT        # fft computing and normaliation
    Y=Y[range(int(NFFT/2))]          # single sied frequency range
    amplitude_Hz = 2*abs(Y)
    phase_ang = np.angle(Y)*180/np.pi
    
    plt.plot(f0,amplitude_Hz,'r')
    plt.title('Single-Sided Amplitude Spectrum of y(t)' + str(check))
    plt.xlabel('frequency($Hz$)')
    plt.ylabel('amplitude')
    plt.xlim(0,4000)
    plt.show()
