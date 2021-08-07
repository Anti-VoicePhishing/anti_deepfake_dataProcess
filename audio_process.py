import matplotlib.pyplot as plt
import numpy as np
from statistics import mean
from scipy.io import wavfile
import wave
import sys
from scipy.io.wavfile import read

plt.figure(1)

def transform(audio):
        """
        audio_input = wave.open(audio,'r')
        signal = audio_input.readframes(-1)
        signal = np.fromstring(signal, 'complex')
        """
        #fr = audio_input.getframerate()
        #time = np.linspace(0, 100, num=(len(signal)))
        
        rate, inwav = read(audio)
        wavarr = np.array(inwav,dtype=complex)
        fft = np.fft.fft(wavarr)
        return fft

class Audio:
    def __init__(self, audio):
        self.audio = wave.open(audio,'r')
        self.signal = self.audio.readframes(-1)
        self.signal = np.fromstring(self.signal, 'float')
        self.fr = self.audio.getframerate()
        self.time = np.linspace(0, 100, num=(len(self.signal)))
        self.fft = np.fft.fft(self.signal)

    def plot(self):
        plt.title("Audio waveforms")
        plt.plot(self.time, self.signal, '.')

#rate, data = wavfile.read("woman.wav")
tf = transform("man.wav")
ifft = np.fft.ifft(tf)
#tf_float = tf.astype(np.float32)
wavfile.write("man_ttf.wav", 44100, ifft.astype(np.int16))

"""
man = Audio('man.wav')
man.plot()
#plt.show()
#wavfile.write("test.wav", 44100, gana)
"""