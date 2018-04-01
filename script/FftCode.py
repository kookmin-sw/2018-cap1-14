import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft
from scipy.io import wavfile # get the api

fs, data = wavfile.read('Air.wav') # load the data
y = data.T[0] # this is a two channel soundtrack, I get the first track
time = data.shape[0] / rate

n = len(y)
NFFT = n
k = np.arange(NFFT)
f0 = k * fs / NFFT
f0 = f0[range(int(NFFT / 2))]

Y = np.fft.fft(part) / NFFT
Y = Y[range(int(NFFT / 2))]

amplitude_Hz = 2 * abs(Y)
phase_ang = np.angle(Y) * 180 / np.pi

plt.plot(f0,amplitude_Hz,'r')
plt.title('Single-Sided Amplitude Spectrum of y(t)' + str(check))
plt.xlabel('frequency($Hz$)')
plt.ylabel('amplitude')
plt.show()
