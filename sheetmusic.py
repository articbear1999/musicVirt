import tkinter as tk
from tkinter import *

def noteTimingDropDown(frame):

	labels = ["Note", "Octave", "Flat or Sharp", "Timing"]
	lab1 = Label(frame, text = labels[0], font = "Arial 8", anchor = 'w')
	lab2 = Label(frame, text = labels[1], font = "Arial 8", anchor = 'w')
	lab3 = Label(frame, text = labels[2], font = "Arial 8", anchor = 'w')
	lab4 = Label(frame, text = labels[3], font = "Arial 8", anchor = 'w')


	notes = ["A", "B", "C", "D", "E", "F", "G"]
	octave = [0, 1, 2, 3, 4, 5, 6, 7, 8]
	flatSharpNot = ["Flat", "Neither", "Sharp"]
	timing = ["1/8", "1/4" , "1/2", "1"]

	notesClicked = StringVar()
	notesClicked.set("A")

	octaveClicked = IntVar()
	octaveClicked.set(4)

	flatSharpNotClicked = IntVar()
	flatSharpNotClicked.set("Neither")

	timingClicked = StringVar()
	timingClicked.set("1/8")


	noteDrop = OptionMenu(frame, notesClicked, *notes)
	octaveDrop = OptionMenu(frame, octaveClicked, *octave)
	flatSharpNotDrop = OptionMenu(frame, flatSharpNotClicked, *flatSharpNot)
	timingDrop = OptionMenu(frame, timingClicked, *timing)

	lab1.pack()
	noteDrop.pack()

	lab2.pack()
	octaveDrop.pack()
	
	lab3.pack()
	flatSharpNotDrop.pack()
	
	lab4.pack()
	timingDrop.pack()