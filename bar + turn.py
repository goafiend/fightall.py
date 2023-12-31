import tkinter as tk
from tkinter.ttk import Progressbar
from tkinter import ttk
import time
parent = tk.Tk()
parent.title("Progressbar")
parent.geometry('350x200')

turn = 1
bar = Progressbar(parent, length=250,
 style='black.Horizontal.TProgressbar')
bar['value'] = 80
bar.grid(column=0, row=0, sticky = "w")
label = tk.Label(text = "Turn: "+ str(turn))
label.grid(column = 0, row = 1, sticky = "w")
time_label = tk.Label()
time_label.grid(column =  0, row= 2, sticky = "w")

def update_label(label):
	global turn
	label.config(text = ("Turn: "+ str(turn)) )
	time_label.config(text = (str(turn/10) + "seconds have passed") )
def barraising():
		global turn
		if(bar['value'] < 101):
			bar['value'] += 1
			turn += 1
			update_label(label)
			parent.after(100, barraising)
			
		else:
			bar['value'] = 0
			parent.after(1000,barraising)
			t.log('bar filled at turn'+str(turn))
			
class TraceConsole():

    def __init__(self):
        # Init the main GUI window
        self._logFrame = tk.Frame(width = 30)
        self._log      = tk.Text(self._logFrame, wrap=tk.NONE, setgrid=True)
        self._scrollb  = tk.Scrollbar(self._logFrame, orient=tk.VERTICAL)
        self._scrollb.config(command = self._log.yview) 
        self._log.config(yscrollcommand = self._scrollb.set)
        # Grid & Pack
        self._log.grid(column=0, row=0)
        self._scrollb.grid(column=1, row=0, sticky=tk.S+tk.N)
        self._logFrame.grid(column = 0, row = 5)


    def log(self, msg, level=None):
        # Write on GUI
        self._log.insert('end', msg + '\n')

    def exitWindow(self):
        # Exit the GUI window and close log file
        print('exit..')
        
cl = TraceConsole()
t.log('hello world!')


barraising()
help(label)
parent.mainloop()


