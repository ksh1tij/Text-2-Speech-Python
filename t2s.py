import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os

root = Tk()
root.title("Text to Speech")
root.geometry("900x450")
root.resizable(False, False)
root.configure(bg="white")

engine = pyttsx3.init()

def speaknow():
    text = text_area.get(1.0, END)
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    voices = engine.getProperty('voices')

    def setvoice():
        if (gender == 'Male'):
            engine.setProperty('voice', voices[0].id)
            engine.say(text)
            engine.runAndWait()
        else:
            engine.setProperty('voice', voices[1].id)
            engine.say(text)
            engine.runAndWait()

    if (text):
        if (speed == 'Fast'):
            engine.setProperty('rate', 250)
            setvoice()
        elif (speed == 'Normal'):
            engine.setProperty('rate', 150)
            setvoice()
        else:
            engine.setProperty('rate', 60)
            setvoice()

def download():
    text = text_area.get(1.0, END)
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    voices = engine.getProperty('voices')

    def setvoice():
        if (gender == 'Male'):
            engine.setProperty('voice', voices[0].id)
            path = filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text, 'text.mp3')
            engine.runAndWait()
        else:
            engine.setProperty('voice', voices[1].id)
            path = filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text, 'text.mp3')
            engine.runAndWait()

    if (text):
        if (speed == 'Fast'):
            engine.setProperty('rate', 250)
            setvoice()
        elif (speed == 'Normal'):
            engine.setProperty('rate', 150)
            setvoice()
        else:
            engine.setProperty('rate', 60)
            setvoice()

#Top frame
Top_frame = Frame(root, bg="#ee5b54", width=900, height = 100)
Top_frame.place(x = 0, y = 0)

Label(Top_frame, bg="#ee5b54").place(x=10,y=5)
Label(Top_frame, text="TEXT TO SPEECH", font="arial 20 bold", bg="#ee5b54", fg="white").place(x=100, y=30)


##########

text_area=Text(root, font="Robote 20", bg="white", relief=GROOVE, wrap=WORD)
text_area.place(x=10, y=150, width=500, height=250)

Label(root, text="VOICE", font="arial 15 bold", bg="white", fg="black").place(x=580,y=160)
Label(root, text="SPEED", font="arial 15 bold", bg="white", fg="black").place(x=760,y=160)

gender_combobox=Combobox(root, values=['Male', 'Female'], font="arial 14", state='r', width=10)
gender_combobox.place(x=550, y=200)
gender_combobox.set('Male')

speed_combobox=Combobox(root, values=['Fast', 'Normal', 'Slow'], font="arial 14", state='r', width=10)
speed_combobox.place(x=730, y=200)
speed_combobox.set('Normal')

btn = Button(root, text="Speak", pady= 15, padx= 20 , compound=LEFT, font="arial 14 bold", command = speaknow)
btn.place(x=560, y=280)

save = Button(root, text="Save", pady= 15, padx= 20 , compound=LEFT, font="arial 14 bold", command = download)
save.place(x=745, y=280)

root.mainloop()