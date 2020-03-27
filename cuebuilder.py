import time
import os
import tkinter as tk
from tkinter import filedialog
from tkinter.scrolledtext import ScrolledText
from os.path import normpath, basename

root = tk.Tk()
root.title("cuebuilder")
hasendtimes = tk.IntVar()
fltype, flname = [""]*2
canvas1 = tk.Canvas(root, width = 700, height = 500)
canvas1.pack()

def debug(obj, line):
	print(obj + " reported at line " + str(line))

# grabs the file name and type from path
def fileio():
	global fltype, flname 
	flname = basename(normpath(filedialog.askopenfilename()))
	fllabel = tk.Label(canvas1, 
		text = flname, fg = "blue", font = ("helvetica", 12, "bold"))
	fltype = flname.split(".")[1]
	flname = flname.split(".")[0]
	if grabfiletype(fltype) == "NOTVALIDAUDIOFMT":
		fllabel.config(text = "ERROR: Please upload a valid audio file type.")
		fllabel.config(fg = "red")
		flname = ""
	canvas1.create_window(400, 100, window = fllabel)

# check if file type is an audio type
def grabfiletype(type):
	audioformats = {"mp3", "ogg", "flac"}
	if type == "wav":
		return "WAVE"
	elif type in audioformats:
		return type.upper()
	else:
		return "NOTVALIDAUDIOFMT"

# enable functionality of entry boxes
def enableafterio():
	if flname:
		genre.configure(state = "normal")
		date.configure(state = "normal")
		mainpfmr.configure(state = "normal")
		albumtitle.configure(state = "normal")
		numsongs.configure(state = "normal")
		splitinfo.configure(state = "normal")
		hasendtimeschk.configure(state = "normal")

# main cue file building
# split info should be loaded like this (values in parentheses valid based on hasendtimes val.):
# [Based on Ryo Fukui's "My Favorite Tune"]
# Voyage 00:00( - 03:32)
# Scenery 03:34( - 07:25)
# Mellow Dream 07:29( - 17:39)
# Nobody knows the trouble I've seen 17:42( - 23:17)
# Nobody's 23:21( - 26:57)
# My Conception 27:01( - 30:47)
# After Hours 30:52( - 38:35)
# Nord 38:38( - 43:32)
def cuebuild(genretxt, datetxt, mainpfmrtxt, albumtitletxt, numsongstxt, splitinfoarr, hasendtimes):
	if flname:
		cf = open("E:/cuebuilder/" + flname + ".cue", "w+")
		cf.write(
			"REM GENRE " + genretxt + "\n" + 
		  "REM DATE " + datetxt + "\n" +
			"PERFORMER \"" + mainpfmrtxt + "\"\n" + 
			"TITLE \"" + albumtitletxt + "\"\n" +
			"FILE \"" + flname + "." + fltype + "\" " + grabfiletype(fltype) + "\n"
		)
		if hasendtimes and isinstance(numsongstxt, int):
			
		elif not hasendtimes and isinstance(numsongstxt, int):
			
		cf.close()

# populating box fields 
genre = tk.Entry(canvas1)
date = tk.Entry(canvas1)
mainpfmr = tk.Entry(canvas1)
albumtitle = tk.Entry(canvas1)
numsongs = tk.Entry(canvas1)
splitinfo = ScrolledText(canvas1)
hasendtimeschk = tk.Checkbutton(canvas1, text = "End Times Are Listed", 
	variable = hasendtimes, font = ("helvetica", 12)) 

# populating label fields 
genrelbl = tk.Label(canvas1, text = "Album Genre", font = ("helvetica", 12))
datelbl = tk.Label(canvas1, text = "Album Date", font = ("helvetica", 12))
mainpfmrlbl = tk.Label(canvas1, text = "Album Artist", font = ("helvetica", 12))
albumtitlelbl = tk.Label(canvas1, text = "Album Title", font = ("helvetica", 12))
numsongslbl = tk.Label(canvas1, text = "# of Songs", font = ("helvetica", 12))
splitinfolbl = tk.Label(canvas1, text = "Song Info", font = ("helvetica", 12))

canvas1.create_window(100, 175, window = genre)
canvas1.create_window(250, 175, window = date)
canvas1.create_window(400, 175, window = mainpfmr)
canvas1.create_window(550, 175, window = albumtitle)
canvas1.create_window(60, 250, width = 40, window = numsongs)
canvas1.create_window(120, 400, window = hasendtimeschk)
canvas1.create_window(345, 300, width = 400, height = 100, window = splitinfo)

canvas1.create_window(100, 150, window = genrelbl)
canvas1.create_window(250, 150, window = datelbl)
canvas1.create_window(400, 150, window = mainpfmrlbl)
canvas1.create_window(550, 150, window = albumtitlelbl)
canvas1.create_window(75, 225, window = numsongslbl)
canvas1.create_window(175, 225, window = splitinfolbl)

genre.configure(state = "disabled")
date.configure(state = "disabled")
mainpfmr.configure(state = "disabled")
albumtitle.configure(state = "disabled")
numsongs.configure(state = "disabled")
splitinfo.configure(state = "disabled")
hasendtimeschk.configure(state = "disabled")

inputbtn = tk.Button(text = "Input file", command = lambda:[fileio(), enableafterio()], 
	bg = "black", fg = "white")
canvas1.create_window(100, 100, window = inputbtn)

# button submition processing
if __name__ == "__main__":
	submittxt = tk.Label(canvas1, 
		text = ".cue file created!", 
		fg = "blue", font = ("helvetica", 12, "bold"))
	submitbtn = tk.Button(text = "Submit", 
		command = lambda:[cuebuild(
			genre.get(), date.get(), mainpfmr.get(), albumtitle.get(), numsongs.get(), 
			splitinfo.get("1.0", tk.END), hasendtimes.get()
			),
			canvas1.create_window(325, 450, window = submittxt)
		],
		bg = "black", fg = "white")
	canvas1.create_window(325, 400, window = submitbtn)

root.mainloop()