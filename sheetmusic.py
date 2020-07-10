import tkinter as tk
from tkinter import *
import pygame
from PIL import Image, ImageTk
from time import sleep

# transform the selection into a note that's recognizable, transform selection of A Sharp 4 to A#4


def addNote(flatSharpNotClicked, notesClicked, octaveClicked, timingClicked, notesList, canvas):
	global sheetMusicNote
	octave = octaveClicked.get()
	notesSel = notesClicked.get()
	flatSharpNot = flatSharpNotClicked.get()
	if octave == "0" and (notesSel != "A" and notesSel != "B"):			# if octave is 0 and its not A or B print msg
		print("The 0th octave only has notes A, A# and B, B# on the piano")
		return
	if octave == "8" and not (notesSel == "C" and flatSharpNot == "Neither"): 	# if octave is 8 and not C, print msg
		print("The 8th octave only has notes C on the piano")
		return
	if notesSel == "A" and flatSharpNot == "Flat" and octave == "0":	# this is corner case for A flat 0
		print("Lowest note is A0")
		return
	if flatSharpNot == "Neither":					# normal case, change flat sharp to empty string
		flatSharpNot = ""
	elif flatSharpNot == "Flat":
		if notesSel == "C" or notesSel == "F":
			print("There's no C flat or F flat on this piano")
			return
		flatSharpNot = "#"
		if notesSel == "A":									# if note is A flat, then change to G#
			notesSel = "G"
		else:
			notesSel = chr(ord(notesSel) - 1)				# if flat drop note down one letter and sharp
	else:
		if notesSel == "E" or notesSel == "B":
			print("There's no E# or B# on this piano")
			return
		flatSharpNot = "#"
	if timingClicked.get() == "1/8":
		timing = .125
		sheetMusicNote = Image.open("eighth.jpg")
		sheetMusicNote = sheetMusicNote.resize((45, 50), Image.ANTIALIAS)
		sheetMusicNote = ImageTk.PhotoImage(sheetMusicNote)  # convert to PhotoImage
	elif timingClicked.get() == "1/4":
		timing = .25
		sheetMusicNote = Image.open("quarter.jpg")
		sheetMusicNote = sheetMusicNote.resize((50, 63), Image.ANTIALIAS)
		sheetMusicNote = ImageTk.PhotoImage(sheetMusicNote)  # convert to PhotoImage
	elif timingClicked.get() == "1/2":
		timing = .5
		sheetMusicNote = Image.open("half.png")
		sheetMusicNote = sheetMusicNote.resize((50, 53), Image.ANTIALIAS)
		sheetMusicNote = ImageTk.PhotoImage(sheetMusicNote)  # convert to PhotoImage
	elif timingClicked.get() == "1":
		timing = 1
		sheetMusicNote = Image.open("whole.png")
		sheetMusicNote = sheetMusicNote.resize((90, 70), Image.ANTIALIAS)
		sheetMusicNote = ImageTk.PhotoImage(sheetMusicNote)  # convert to PhotoImage

	canvNote = canvas.create_image(len(notesList) * 100 + 150, 63, image=sheetMusicNote)
	canvas.tag_lower(canvNote)
	notesList.append([notesSel + flatSharpNot + octave, timing])		# add note to the notesList
	'''
	global eighth
	global quarter
	global half
	global whole

	eighth = Image.open("eighth.jpg")
	eighth = eighth.resize((45, 50), Image.ANTIALIAS)
	eighth = ImageTk.PhotoImage(eighth)  # convert to PhotoImage
	quarter = Image.open("quarter.jpg")
	quarter = quarter.resize((50, 63), Image.ANTIALIAS)
	quarter = ImageTk.PhotoImage(quarter)  # convert to PhotoImage
	half = Image.open("half.png")
	half = half.resize((50, 53), Image.ANTIALIAS)
	half = ImageTk.PhotoImage(half)  # convert to PhotoImage
	whole = Image.open("whole.png")
	whole = whole.resize((90, 70), Image.ANTIALIAS)
	whole = ImageTk.PhotoImage(whole)  # convert to PhotoImage
	canvEighth = canvas.create_image(150, 63, image=eighth)
	canvas.tag_lower(canvEighth)
	canvQuart = canvas.create_image(250, 63, image=quarter)
	canvas.tag_lower(canvQuart)
	canvHalf = canvas.create_image(350, 63, image=half)
	canvas.tag_lower(canvHalf)
	canvWhole = canvas.create_image(450, 63, image=whole)
	canvas.tag_lower(canvWhole)
	'''
	print(notesList)


# delete notes from the notesList
def delNote(notesList):
	if not notesList:									# if list is empty
		print("list of notes is empty, cannot remove")
		return
	notesList.pop()


def playNote(note_played):                            # takes a note name and the octave to determine wav file to play
        note_played = "piano_sounds" + '\\'+ note_played + ".wav"
        sound = pygame.mixer.Sound(note_played)
        sound.play()
        return


# play the whole list of notes
def playNoteList(note_list):
	for i in note_list:
		note_played = "piano_sounds" + '\\' + i[0] + ".wav"
		sound = pygame.mixer.Sound(note_played)
		sound.play()
		pygame.time.delay(int(2000 * i[1]))
	return


def noteTimingDropDown(frame, notesList, canvas):

	labels = ["Note", "Octave", "Flat or Sharp", "Timing"]
	lab1 = Label(frame, text=labels[0], font="Arial 8", anchor='w')
	lab2 = Label(frame, text=labels[1], font="Arial 8", anchor='w')
	lab3 = Label(frame, text=labels[2], font="Arial 8", anchor='w')
	lab4 = Label(frame, text=labels[3], font="Arial 8", anchor='w')

	# create drop down list
	notes = ["C", "D", "E", "F", "G", "A", "B"]
	octave = [0, 1, 2, 3, 4, 5, 6, 7, 8]
	flatSharpNot = ["Flat", "Neither", "Sharp"]
	timing = ["1/8", "1/4" , "1/2", "1"]

	# create string variables and default values
	notesClicked = StringVar()
	notesClicked.set("A")

	octaveClicked = StringVar()
	octaveClicked.set(4)

	flatSharpNotClicked = StringVar()
	flatSharpNotClicked.set("Neither")

	timingClicked = StringVar()
	timingClicked.set("1/8")

	# create drop down menus
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

	addButton = Button(frame, text="add note", command=
				lambda: addNote(flatSharpNotClicked, notesClicked, octaveClicked, timingClicked, notesList, canvas))
	addButton.pack()

	deleteButton = Button(frame, text="delete note", command=lambda: delNote(notesList))
	deleteButton.pack()

	playButton = Button(frame, text="play", command=lambda: playNoteList(notesList))
	playButton.pack()


def drawSheet(canvas):
	# draw the treble cleft
	global treble
	treble = Image.open("treble.gif")
	treble = treble.resize((100, 100), Image.ANTIALIAS)
	treble = ImageTk.PhotoImage(treble)  # convert to PhotoImage
	canvas.create_image(50, 50, image=treble)

	# draw the five lines
	canvas.create_line(0, 20, 1200, 20)
	canvas.create_line(0, 40, 1200, 40)
	canvas.create_line(0, 60, 1200, 60)
	canvas.create_line(0, 80, 1200, 80)
	canvas.create_line(0, 100, 1200, 100)

