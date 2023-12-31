import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import *
#bar in green with text
my_w = tk.Tk()
my_w.geometry("400x300")

s = ttk.Style()
print(ttk.Style().theme_names())
s.theme_use('classic')
s.configure("default.Horizontal.TProgressbar")
s.configure("red.Horizontal.TProgressbar", background = "red", fg = "red")
s.configure("yellow.Horizontal.TProgressbar", background = "yellow")
s.configure("blue.Horizontal.TProgressbar", background = "blue")
s.configure("green.Horizontal.TProgressbar", background = "green")
l1 = tk.Label(my_w, text = "Progressbar style changing")
l1.grid(row = 0, column = 0)

def my_upd(value):
    prg1['value']=my_scale1.get()

prg1=ttk.Progressbar(my_w, orient = HORIZONTAL,  length = 320, mode = "determinate", maximum = 100, style = "yellow.Horizontal.TProgressbar",
                     value = 75)
prg1.grid(row = 1, column = 0, columnspan = 3, padx = 20, pady = 45)
print(prg1.winfo_class())
b1 = tk.Button(my_w, text = "Red", bg= "red", font = 20,
               command = lambda:prg1.config(style="red.Horizontal.TProgressbar"))
b1.grid(row = 2, column = 0)
b2 = tk.Button(my_w, text = "yellow", bg= "yellow", font = 20,
               command = lambda:prg1.config(style="yellow.Horizontal.TProgressbar"))
b2.grid(row = 2, column = 1)
b3 = tk.Button(my_w, text = "blue", bg= "blue", font = 20,
               command = lambda:prg1.config(style="blue.Horizontal.TProgressbar"))
b3.grid(row = 2, column = 2)
b4 = tk.Button(my_w, text = "green", bg= "green", font = 20,
               command = lambda:prg1.config(style="green.Horizontal.TProgressbar"))
b4.grid(row = 2, column = 3)
b5 = tk.Button(my_w, text = "default", bg= "white", font = 20,
               command = lambda:prg1.config(style="default.Horizontal.TProgressbar"))
b5.grid(row = 2, column = 4)

my_scale1 = tk.Scale(my_w, from_ = 0, to = 100, orient ="horizontal", command = my_upd, length = 200)
my_scale1.grid(row = 3, column = 0, columnspan = 3)

my_w.mainloop()