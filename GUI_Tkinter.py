import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter import *
import math
from PIL import Image, ImageTk
import time



# Create instance
window = tk.Tk()
# Add a title
window.title("window")
#Decide size
SCALE = 20
WINDOW_WIDTH = SCALE * 50
WINDOW_HEIGHT = SCALE * 20
window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

def generate_bar(bar_value, bar_pos_x, bar_pos_y, frame = window):

    bar = ttk.Progressbar(
        frame,
        orient='horizontal',
        mode='determinate',
        length=SCALE * 6,
        value = bar_value,
    )
    bar.grid(column=bar_pos_x, row=bar_pos_y, columnspan=1, padx=SCALE / 2, pady=SCALE / 2)
    return bar

def update_bar(bar, bar_value):
    bar.config(value = bar_value)

def generate_label(label_name, label_text, label_pos_x = 0, label_pos_y = 0, frame = window ):

    label = tk.Label(frame, font=("Arial", (math.floor(SCALE / 2))), fg="Black", name = label_name)
    label.grid(column = label_pos_x, row = label_pos_y)
    update_label(label, label_text)
    return label


def update_label(label, label_text):
    label.config(text = str(label_text))

def generate_button(button_text, button_pos_x, button_pos_y, frame = window):
     button_function = get_entry
     button = tk.Button(frame, text= str(button_text), command= button_function)
     button.grid(column = button_pos_x, row = button_pos_y)

def generate_entry(entry_pos_x, entry_pos_y, frame = window):
    global entryfield
    entryfield = Entry(frame, width= 30, borderwidth = 5)
    entryfield.grid(column = entry_pos_x, row = entry_pos_y)

def get_entry():
    global entryfield
    e = entryfield.get()
    print(e)

img = Image.open("pictures/Target.jpg")
image1 = ImageTk.PhotoImage(img)
target_sign = Label(window, image=image1)




def start_window():
    window.mainloop()