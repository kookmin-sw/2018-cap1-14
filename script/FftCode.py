import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft
from scipy.io import wavfile # get the api

fs, data = wavfile.read('Air.wav') # load the data
y = data.T[0] # this is a two channel soundtrack, I get the first track
time = data.shape[0] / rate
