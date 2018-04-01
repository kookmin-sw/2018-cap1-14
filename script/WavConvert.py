#required libraries
import urllib
import scipy.io.wavfile
import pydub

#read mp3 file
mp3 = pydub.AudioSegment.from_mp3("Air.mp3")
#convert to wav
mp3.export("Air.wav", format="wav")
