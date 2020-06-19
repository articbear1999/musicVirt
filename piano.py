#'''
import pygame
import sys
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, ifft
import scipy.io.wavfile as wave

pygame.init()

freqList = [pow(2, (i-49)/12)*440 for i in range(1, 89)] # create a list of frequencies with the indices as the note
                                                        # starts from 1, so the formula works
noteList = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
whiteKeyList = ["A", "B", "C", "D", "E", "F", "G"]
blackKeyList = ["A#", "", "C#", "D#", "", "F#", "G#"]


def freq_to_note(freq):
        noteNum = findClosest(freqList, 88, freq)      # return index of given freq on what numNote to play
        return noteNum
        #return noteList[noteNum % 12]                  # return that num in terms of the key that it corresponds to

# findClosest, getClosest pulled straight from geeksforgeeks, minor tweaks to return index instead of value
def findClosest(arr, n, target):                        # returns the index of the closest given value in an array
        # Corner cases
        if (target <= arr[0]):
                return 0
        if (target >= arr[n - 1]):
                return n - 1

                # Doing binary search
        i = 0
        j = n
        mid = 0
        while (i < j):
                mid = (i + j) // 2

                if (arr[mid] == target):
                        return mid

                        # If target is less than array
                # element, then search in left
                if (target < arr[mid]):

                        # If target is greater than previous
                        # to mid, return closest of two
                        if (mid > 0 and target > arr[mid - 1]):
                                return getClosest(arr[mid - 1], arr[mid], mid - 1, mid, target)

                                # Repeat for left half
                        j = mid

                        # If target is greater than mid
                else:
                        if (mid < n - 1 and target < arr[mid + 1]):
                                return getClosest(arr[mid], arr[mid + 1], mid, mid + 1, target)

                                # update i
                        i = mid + 1

        # Only single element left after search
        return mid


# Method to compare which one is the more close.
# We find the closest by taking the difference
# between the target and both values. It assumes
# that val2 is greater than val1 and target lies
# between these two.
def getClosest(val1, val2, val1Index, val2Index, target):
        if (target - val1 >= val2 - target):
                return val2Index
        else:
                return val1Index


infile = "twinkle.wav"
rate, data = wave.read(infile)
scale = 1                                                       # scale of 10 means 10 samples per sec
sample_rate = int(rate/scale)
time_frames = [data[i:i + sample_rate] for i in range(0, len(data), sample_rate)]
notes = []
for x in range(len(time_frames)):                               # for each section, get the FFT
        data = np.array(time_frames[x])                         # convert to np array
        frequencies = np.fft.fft(data)                          # get the FFT of the wav file
        inverse = ifft(np.real(frequencies))
        '''
        plt.subplot(2, 1, 1)
        plt.plot(data)
        plt.title("Original wave: " + infile)

        plt.subplot(2, 1, 2)
        plt.plot(np.abs(frequencies))
        plt.title("Fourier transform results")

        # plt.xlim(0, 10000)

        plt.tight_layout()

        plt.show()
        '''
        index_max = np.argmax(np.abs(frequencies[0:1000//scale]))      # get the index of the max number within music range
        index_max = index_max*scale
        notes.append(freq_to_note(index_max))
        print(index_max)

print(notes)


def playNote(note):                                     # takes a note name and the octave to determine wav file to play
        note = "piano_sounds" + '\\'+ note + ".wav"
        sound = pygame.mixer.Sound(note)
        sound.play()
        return


piano = tk.Tk()
frame = tk.Frame(piano)
frame.pack()

blackKeys = tk.Frame(piano)
blackKeys.pack(side=tk.TOP)

piano.title('PIANO')
blackKeyButtons = []
for i in range (0, 51):
        note = blackKeyList[i % 7]
        octave = str(i // 7) if (i % 7 == 0) else str(i // 7 + 1)
        noteParam = note + octave                       # get the note name and the octave to pass into playNote
        if (i % 7) == 1 or (i % 7) == 4:                # notes that don't exist draw blanks
                buttonBlank = tk.Button(blackKeys, state=tk.DISABLED, padx=8, height=6, width=1, pady=8, bd=0,
                                        bg="white",fg="white", activebackground="red")
                buttonBlank.pack(side=tk.LEFT)
        else:                                           # pentatonic notes, text you get from blackKeyList
                buttonBlack = tk.Button(blackKeys, padx=4, height=6, width=1, pady=8, bd=4,
                                        text=blackKeyList[i % 7], bg="black", fg="white",
                                        activebackground="red", command=lambda noteParam=noteParam: playNote(noteParam))
                buttonBlack.pack(side=tk.LEFT)
                blackKeyButtons.append(buttonBlack)

whiteKeys = tk.Frame(piano)
whiteKeys.pack(side=tk.TOP)
whiteKeyButtons = []
for i in range (0, 52):                                  # code white keys, text you get from the whitKeyList
        note = whiteKeyList[i % 7]
        octave = str(i//7) if (i % 7 == 0 or i % 7 == 1) else str(i//7+1)
        noteParam = note + octave
        buttonWhite = tk.Button(whiteKeys, padx=4, height=6, width=1, pady=8, bd=4,
                                text=note, fg="black",
                                activebackground="red", command=lambda noteParam=noteParam: playNote(noteParam))
        buttonWhite.pack(side=tk.LEFT)
        whiteKeyButtons.append(buttonWhite)

buttonConversion = [0, 0, 1, 2, 1, 3, 2, 4, 5, 3, 6, 4]
COUNTER = 0
def triggerButton():
        global COUNTER
        if COUNTER == len(notes):
                piano.after_cancel(play)
                return
        num = notes[COUNTER]
        COUNTER = COUNTER + 1
        octave = num // 12
        num = num % 12
        if num == 1 or num == 4 or num == 6 or num == 9 or num == 11:
                index = octave * 5 + buttonConversion[num]
                blackKeyButtons[index].invoke()
        else:
                index = octave * 7 + buttonConversion[num]
                whiteKeyButtons[index].invoke()
        piano.after(1000//scale, triggerButton)


play = piano.after(1000//scale, triggerButton)
piano.mainloop()

'''
data = np.array(data)

data_fft = np.fft.fft(data)
frequencies = (data_fft)
inverse = ifft(np.real(frequencies))
print(np.real(inverse))

plt.subplot(2,1,1)
plt.plot(data)
plt.title("Original wave: " + infile)

plt.subplot(2,1,2)
plt.plot(np.abs(frequencies))
plt.title("Fourier transform results")

#plt.xlim(0, 10000)

plt.tight_layout()

plt.show()
'''
#wave.write('out2.wav',rate,np.real(inverse))
#'''
