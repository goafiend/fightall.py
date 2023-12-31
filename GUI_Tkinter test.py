import GUI_Tkinter as gui
import math




menuframe = gui.tk.Frame(gui.window, width=400, height=500, bg='black')
menuframe.grid(column = 0, row = 0, padx=10, pady=10)
bar1 = gui.generate_bar( 20, 1,1, menuframe)
bar2 = gui.generate_bar( 25, 1,2, menuframe)
label =  gui.generate_label("namedwd", "frame is up", 2, 0, menuframe )
print(bar1)


print(bar2)
gui.start_window()