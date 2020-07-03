#'''
import pygame
import sys
from  sheetmusic import  *
from reader import read_data

whiteKeyList = ["A", "B", "C", "D", "E", "F", "G"]
blackKeyList = ["A#", "", "C#", "D#", "", "F#", "G#"]
notes = []
piano = None
scale = 10                                                      # scale of 10 means 10 samples per sec

def main():
        global notes
        global piano
        pygame.init()
        
       # notes = read_data(scale)
        print(notes)
        piano = tk.Tk()
        piano.title('PIANO')
        
        piano_construct() #helper methods for drawing the keys on the piano
        
        frame = tk.Frame(piano)
        frame.pack()
        noteTimingDropDown(frame)
        play = piano.after(0, triggerButton)          # do action while main loop is going for GUI
        piano.mainloop()

def piano_construct():
        blackKeys = tk.Frame(piano)                             # black keys are in top frame
        blackKeys.pack(side=tk.TOP)
        blackKeyButtons = []
        for i in range (0, 51):
                note = blackKeyList[i % 7]
                octave = str(i // 7) if (i % 7 == 0) else str(i // 7 + 1)
                noteParam = note + octave                       # concatenate the two strings to get note and octave ie. C#7
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

        whiteKeys = tk.Frame(piano)                             # push white key frame into the next top frame possible
        whiteKeys.pack(side=tk.TOP)
        whiteKeyButtons = []
        for i in range (0, 52):                                 # code white keys, text you get from the whitKeyList
                note = whiteKeyList[i % 7]
                octave = str(i//7) if (i % 7 == 0 or i % 7 == 1) else str(i//7+1)
                noteParam = note + octave                       # concatenate the two strings to get note and octave ie. C7
                buttonWhite = tk.Button(whiteKeys, padx=4, height=6, width=1, pady=8, bd=4,
                                        text=note, fg="black",
                                        activebackground="red", command=lambda noteParam=noteParam: playNote(noteParam))
                buttonWhite.pack(side=tk.LEFT)
                whiteKeyButtons.append(buttonWhite)

def playNote(note_played):                                     # takes a note name and the octave to determine wav file to play
        note_played = "piano_sounds" + '\\'+ note_played + ".wav"
        sound = pygame.mixer.Sound(note_played)
        sound.play()
        return


COUNTER = 0
def triggerButton():                            # this will be called to play the song inputted
        global COUNTER
        global piano
        if COUNTER == len(notes):               #if played whole song, stop playing
                piano.after_cancel(play)
                return
        num = notes[COUNTER]
        COUNTER = COUNTER + 1
        octave = num // 12 + 1
        num = num % 12
        
        buttonConversion = [0, 0, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6]  # black keys are in indices 1,4,6,9,11, whites keys in others
        index = buttonConversion[num]
        if num == 1 or num == 4 or num == 6 or num == 9 or num == 11:   # if black key, call the corresponding black key
                octave = octave - 1 if (index == 0) else octave
                note = blackKeyList[index]
                playNote(note+str(octave))
                #blackKeyButtons[index].flash()
        else:                                                           # if white key, call the corresponding white key
                octave = octave - 1 if (index == 0 or index == 1) else octave
                note = whiteKeyList[index]
                playNote(note+str(octave))
                #whiteKeyButtons[index].flash()
        piano.after(1000//scale, triggerButton)                         # call after again until the song is over



if __name__ == "__main__":
    main()