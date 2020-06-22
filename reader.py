import scipy.io.wavfile as wave
import numpy as np
from frequencyUtil import *
from scipy.fft import fft, ifft

def read_data(scale):
        infile = "silent.wav"
        rate, data = wave.read(infile)
        sample_rate = int(rate/scale)
        time_frames = [data[i:i + sample_rate] for i in range(0, len(data), sample_rate)]
        notes = []
        for x in range(len(time_frames)):                               # for each section, get the FFT
                data = np.array(time_frames[x])                         # convert to np array
                dataZero = [row[0] for row in data]
                #print(dataZero)
                frequencies = np.fft.fft(dataZero)                          # get the FFT of the wav file
                inverse = ifft(np.real(frequencies))

                #We need to figure out what to do with 0:1000 cause notes can go above
                index_max = np.argmax(np.abs(frequencies[0:2000//scale]))      # get the index of the max number within music range
                #filters out the amplitudes that are lower than this value found through testing
                # should eventually understand the scale of the fft frequenices
                #print(abs(frequencies[index_max]))
                if(abs(frequencies[index_max]) < 4000000/scale):
                       continue
                index_max = index_max*scale
                notes.append(freq_to_note(index_max))
        return notes
