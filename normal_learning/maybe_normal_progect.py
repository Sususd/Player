import virtualenv
from tkinter import *
import tkinter.ttk as ttk
import tkinter as tk
from pygame import mixer
import pygame
import os
import sys
from tkinter.messagebox import showinfo
import tkinter.filedialog as filedialog
import time
from mutagen.mp3 import MP3


pygame.init()
mixer.init()

def play_time():
	current_time = mixer.music.get_pos() / 1000
	converted_current_time = time.strftime('%H:%M:%S', time.gmtime(current_time))
	status_bar.config(text = converted_current_time)

	status_bar.after(1000, play_time)

def playsong():
	currentsong = playlist.get(ACTIVE)
	print(currentsong)
	mixer.music.load(currentsong)
	mixer.music.play()

	play_time()

def pausesong():
        mixer.music.pause()

def stopsong():
        mixer.music.stop()

def resumesong():
        mixer.music.unpause()

rootpath = ""
pattern = "*.mp3"

def play_next():
        next_song = playlist.curselection()
        next_song = next_song[0] + 1
        next_song_name = playlist.get(next_song)
        label.config(text = next_song_name)
        mixer.music.load(rootpath + next_song_name)
        mixer.music.play()
        playlist.select_clear(0, "end")
        playlist.activate(next_song)
        playlist.select_set(next_song)

def play_prev():
	next_song = playlist.curselection()
	next_song = next_song[0] - 1
	next_song_name = playlist.get(next_song)
	label.config(text = next_song_name)
	mixer.music.load(rootpath + next_song_name)
	mixer.music.play()
	playlist.select_clear(0, "end")
	playlist.activate(next_song)
	playlist.select_set(next_song)

window = Tk()
window.geometry("453x250")
window.title("Music player")

icon = PhotoImage(file = 'logo.png')
window.iconphoto(True, icon)

bg = PhotoImage(file = "background1.png")
label = Label( window,
	image = bg)
label.place(x=0, y=0)

def volume(x):
	mixer.music.set_volume(w.get())

w = ttk.Scale(window,
	from_ = 0,
	to = 1,
	command = volume,
	orient = HORIZONTAL)
w.pack()
w.place(x=5, y=190)

playlist = Listbox(window,
        selectmode=SINGLE,
	width = 61,
	height = 8,
        foreground = 'white',
	background = 'black')
playlist.pack()
playlist.place(x=6, y=10)

os.chdir('/home/manjus/Музыка')
song = os.listdir()

for s in song:
        playlist.insert(END,s)

btn = Button(window,
	text = '⫸',
	command = playsong,
	width = 5,
	background = '#458')
btn.pack()
btn.place(x=130, y=157)

btn = Button(window,
	text = '||',
	command = pausesong,
	width = 5,
	background = '#390')
btn.pack()
btn.place(x=195, y=187)

btn = Button(window,
	text = '⋫',
	command = stopsong,
	width = 5,
	background = '#458')
btn.pack()
btn.place(x=130, y=187)

btn = Button(window,
	text = '⊳',
	command = resumesong,
	width = 5,
	background = '#390')
btn.pack()
btn.place(x=195, y=157)

btn = Button(window,
	text = '▶▶',
	command = play_next,
	width = 5,
	background = 'purple')
btn.pack()
btn.place(x=260, y=157)

btn = Button(window,
        text = '◀◀',
	command = play_prev,
	width = 5,
	background = 'purple')
btn.pack()
btn.place(x=260, y=187)

def exit():
	window.destroy()

btn = Button(window,
	text = 'exit',
	command = exit,
	background = '#900')
btn.pack()
btn.place(x=403, y=180)

status_bar = Label(window,
	text = '',
	bd = 1,
	relief = GROOVE,
	anchor = E,
	background = 'black',
	foreground = 'white')
status_bar.pack(fill = X, side = BOTTOM, ipady = 2)

window.resizable(False, False)
window.mainloop()
