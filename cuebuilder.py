import time
import os
import tkinter as tk
from tkinter import filedialog
from os.path import normpath, basename

hasEndTimes = False
fltype, flname = [""]*2
root = tk.Tk()
root.title("cuebuilder")
#root.withdraw()
canvas1 = tk.Canvas(root, width = 1000, height = 500)
canvas1.pack()

def debug(obj, line):
	print(obj + " reported at line " + str(line))

def fileio():
	# grabs the file name and type from path
	global fltype, flname 
	flname = basename(normpath(filedialog.askopenfilename()))
	fltype = flname.split(".")[1]
	flname = flname.split(".")[0]
	fllabel = tk.Label(canvas1, 
		text = flname, 
		fg = "blue", font = ("helvetica", 12, "bold"))
	canvas1.create_window(600, 100, window = fllabel)

#def buildsonggui():

# def cuebuild(flname, fltype, genre, date, mainpfmr, albumtitle, 
#		splitinfo, numSongs, hasEndTimes)
# main building
def cuebuild():
	if flname:
		cf = open("E:/cuebuilder/" + flname + ".cue", "w+")
		cf.write("configuring done.")
		cf.close()

genre = tk.Entry(canvas1)
date = tk.Entry(canvas1)
mainpfmr = tk.Entry(canvas1)
albumtitle = tk.Entry(canvas1)
numSongs = tk.Entry(canvas1)

genrelbl = tk.Label(canvas1, text = "Album Genre", 
	fg = "black", font = ("helvetica", 12))
datelbl = tk.Label(canvas1, text = "Album Date", 
	fg = "black", font = ("helvetica", 12))
albumtitlelbl = tk.Label(canvas1, text = "Album Title", 
	fg = "black", font = ("helvetica", 12))
mainpfmrlbl = tk.Label(canvas1, text = "Main Performer", 
	fg = "black", font = ("helvetica", 12))

canvas1.create_window(200, 175, window = genre)
canvas1.create_window(400, 175, window = date)
canvas1.create_window(200, 150, window = genrelbl)
canvas1.create_window(400, 150, window = datelbl)

#genre.configure(state = "disabled")

inputbtn = tk.Button(text = "Input file", command = fileio, 
	bg = "black", fg = "white")
canvas1.create_window(200, 100, window = inputbtn)

if __name__ == "__main__":
	debug(flname, 66)
	submitbtn = tk.Button(text = "Submit", 
		command = cuebuild, 
		bg = "black", fg = "white")
	canvas1.create_window(400, 400, window = submitbtn)

root.mainloop()