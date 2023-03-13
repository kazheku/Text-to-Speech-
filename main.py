import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3

root = Tk()
root.title("Text to speech made by Kazsuner")
root.geometry("900x450")
root.resizable(False, False)
root.configure(bg="#6643A4")

engine = pyttsx3.init()

def speaknow():
    text = text_area.get("1.0", END).strip()
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    rate = {"Fast": 250, "Normal": 150, "Slow": 60}[speed]

    voices = engine.getProperty('voices')
    voice = {"Male": voices[0].id, "Female": voices[1].id}[gender]
    engine.setProperty('voice', voice)
    engine.setProperty('rate', rate)
    engine.say(text)
    engine.runAndWait()

def download():
    text = text_area.get("1.0", END).strip()
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    rate = {"Fast": 250, "Normal": 150, "Slow": 60}[speed]

    voices = engine.getProperty('voices')
    voice = {"Male": voices[0].id, "Female": voices[1].id}[gender]
    engine.setProperty('voice', voice)
    engine.setProperty('rate', rate)
    filename = filedialog.asksaveasfilename(defaultextension='.mp3')
    if filename:
        engine.save_to_file(text, filename)
        engine.runAndWait()

# Top Frame
Top_frame = Frame(root, bg="white", width=900, height=100)
Top_frame.place(x=0, y=0)

Label(Top_frame, text="Text to speech", font="arial 30 bold", bg="white", fg="black").place(x=20, y=30)

# Text area - Settings
text_area = Text(root, font="Verdana 15", bg="white", relief=GROOVE, wrap=WORD)
text_area.place(x=20, y=150, width=500, height=250)

# Gender - Settings
gender_combobox = Combobox(root, values=['Male', 'Female'], font="Arial 12", state='readonly', width=10)
gender_combobox.place(x=550, y=200)
gender_combobox.current(0)

# Speed - Settings
speed_combobox = Combobox(root, values=['Fast', 'Normal', 'Slow'], font="Arial 12", state='readonly', width=10)
speed_combobox.place(x=730, y=200)
speed_combobox.current(1)

# Speak btn - Settings
btn = Button(root, text="Speak", width=10, bg="#4B4453", fg="white" ,font="Arial 14 bold", command=speaknow)
btn.place(x=550, y=360)

# Save btn - Settings
save = Button(root, text="Save", width=10, bg="#4B4453", fg="white",font="Arial 14 bold", command=download)
save.place(x=730, y=360)

root.mainloop()
