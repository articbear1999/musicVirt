import scipy.io.wavfile as wave
import numpy as np
from frequencyUtil import *
from scipy.fft import fft, ifft
from matplotlib import pyplot as plt
def read_data(scale):
        fs = 44100
        samples = np.linspace(0, 1, int(fs*1), endpoint=False)
        signal = np.sin(2 * np.pi * 1050 * samples)
        signal *= 32767
        signal = np.int16(signal)
        notes = []
        frequencies = fft(signal)
        plt.plot(abs(np.real(frequencies)))
        plt.show()