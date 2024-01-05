#TODOS:
# design Combatlog better
# Separate Combat display from general displaying functions
# fix multiple lvlupsdisplay
# Tooltips
# widgets as Classes


import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter import *
import math
from PIL import Image, ImageTk
import time

# Create instance
combat = tk.Tk()
scale = 20
combatscreen_width = scale * 50
combatscreen_height = scale * 30
combatscreen_width_free = combatscreen_width
combatscreen_height_free = combatscreen_height
combat.geometry(f"{combatscreen_width}x{combatscreen_height}")
combat.update_idletasks()

def print_widget_size(widget, widget_name):
    widget.update_idletasks()
    size_info = f"{widget_name} Size: {widget.winfo_width()} x {widget.winfo_height()}"
    print(size_info)


# Add a title
combat.title("combat")

print_widget_size(combat, "combat")
pause = True


img = Image.open("pictures/target.jpg")
target_img = ImageTk.PhotoImage(img)
img = Image.open("pictures/not_target.jpg")
not_target_img = ImageTk.PhotoImage(img)

s = ttk.Style()
s.theme_use('default')
s.configure("red.Horizontal.TProgressbar", background = "red")
s.configure("yellow.Horizontal.TProgressbar", background = "yellow")
s.configure("blue.Horizontal.TProgressbar", background = "blue")
s.configure("green.Horizontal.TProgressbar", background = "green")

class Unit_display:
    def __init__(self, frame, posx, posy, name_label, health_bar, health_label, action_label, action_bar, target_button, experience_bar, experience_label, rows):
        self.frame = frame
        self.posx = posx
        self.posy = posy
        self.name_label = name_label
        self.health_bar = health_bar
        self.health_label = health_label
        self.action_label = action_label
        self.action_bar = action_bar
        self.target_button = target_button
        self.experience_bar = experience_bar
        self.experience_label = experience_label
        self.rows = rows
unit_displays = []

class Combatlog():

    def __init__(self, log_master, log_width, log_height, log_x, log_y, log_columnspan):
        # Init the main GUI window
        self._logFrame = tk.Frame(log_master, width = log_width, height = log_height)
        self._log      = tk.Text(self._logFrame, wrap=tk.WORD, setgrid=True, width= math.floor(log_width*0.8), height = math.floor(log_height * 0.8))
        self._scrollb  = tk.Scrollbar(self._logFrame, orient=tk.VERTICAL)
        self._scrollb.config(command = self._log.yview)
        self._log.config(yscrollcommand = self._scrollb.set)
        # Grid
        self._logFrame.grid(column = log_x, row = log_y, columnspan = log_columnspan)
        self._log.grid(column=0, row=0)
        self._scrollb.grid(column=1, row=0)
        print_widget_size(self._logFrame, "logframe")
        print_widget_size(self._log, "log")
        print_widget_size(self._scrollb, "scrollb")
    def log(self, msg, level=None):
        # Write on GUI
        self._log.insert('end', msg + '\n')


def turn_label_text(turn):
    text = f"Turn: {turn}"
    return text

def time_label_text(runtime):
    text = f"{math.floor(runtime)} s since start"
    return text

def health_label_text(health, maxhealth):
    text = f"Health:{health}/{maxhealth}"
    return text

def health_bar_value(health, maxhealth):
    value = health/maxhealth * 100
    return value

def action_label_text(turn, action_start, action_end):
    text = f"Attack in {str(math.floor((action_end-turn)/10)/10)}s"
    return text
def action_bar_value(turn, action_start, action_end):
    value = ((turn-action_start)/(action_end - action_start)) * 100
    return value

def damage_label_text(damage):
    text= f"Damage: {str(damage)}"
    return text

def experience_label_text(xp, xptolv, owner):
    if owner == "player":
        text = f"XP: {math.floor(xp)} / {xptolv}"
    if owner == "computer":
        text = f"XPreward: {math.floor(xp)}"
    return text

def experience_bar_value(xp, xptolv, owner):
    if(owner == "player"):
        value = xp/xptolv * 100
    if(owner == "computer"):
        value = xp/xptolv * 100
    return value

def generate_menu(menu_pos_x, menu_pos_y, turn):
    x = menu_pos_x
    y = menu_pos_y
    global scale
    menu_height = scale * 2
    menu_width = combatscreen_width
    print(f"{combatscreen_width =}")
    menu_frame = tk.Frame(combat, width=menu_width, height=menu_height)
    menu_frame.grid(column = x ,row = y, columnspan = 5)
    global combatscreen_width_free
    combatscreen_width_free -= menu_width
    print(combatscreen_width_free)

    menu_frame.update_idletasks()
    print_widget_size(menu_frame, "Menu_frame")

    global turn_label
    turn_label = generate_label(menu_frame, turn_label_text(turn), x, y)
    x += 1

    global time_label
    time_label = generate_label(menu_frame,  time_label_text(0), x, y)
    x += 1

    global pause_continue_button
    pause_continue_button = tk.Button(menu_frame, text="Fight", command=pause_continue)
    pause_continue_button.grid(column = x, row = y)
    x += 1


def generate_combat_window(units):
    combat.bind(('<space>'), lambda event: pause_continue())
    turn = 0
    generate_menu(0,0, turn)
    i = 0
    global cl
    print(f"{scale =}")
    cl = Combatlog(combat,scale * 5, scale,0, 2222, 5)
    print(cl)
    print_widget_size(cl._logFrame, "cl._logframe")

    unit_display_width = 100
    for unit in units:
        print(f"Unit display number {i} starts generating")
        generate_unit_display(unit, turn, 1 + i, 1, i, unit_display_width)
        if unit.owner == "player":
            start_target = unit.target
        i += 1

    on_target_click(start_target, 0)
def generate_unit_display(unit, turn, pos_x, pos_y, index, unit_display_width):
    x = pos_x
    y = pos_y
    unit_frame = tk.Frame(combat, width=unit_display_width, height=250)
    unit_frame.grid(column = x, row = y)
    unit_frame.update_idletasks()
    print_widget_size(unit_frame, "unit_frame")
    x = 0
    y = 0

    name_label = generate_label(unit_frame, unit.name, x, y)
    y += 1
    health_bar = generate_bar(unit_frame, health_bar_value(unit.health, unit.maxhealth), x, y, "red.Horizontal.TProgressbar")
    y += 1
    health_label = generate_label(unit_frame, health_label_text(unit.health, unit.maxhealth), x, y, "red")
    y += 1
    damage_label = generate_label(unit_frame, damage_label_text(unit.damage), x, y, "brown")
    y+=1
    action_label = generate_label(unit_frame, action_label_text(turn, unit.action_start, unit.action_end), x, y,"#d68910")
    y += 1
    action_bar = generate_bar(unit_frame, action_bar_value(turn, unit.action_start, unit.action_end), x, y, "yellow.Horizontal.TProgressbar")
    y += 1
    target_button = tk.Button(unit_frame, image = not_target_img, command=lambda n=index: on_target_click(n, target))
    y += 1
    target_button.grid(column=x, row=y)
    y += 1
    experience_bar = generate_bar(unit_frame, 0, x, y,"blue.Horizontal.TProgressbar")
    y += 1
    experience_label = generate_label(unit_frame, experience_label_text(unit.xp,unit.xptolv, unit.owner), x, y)
    unit_displays.append(Unit_display(unit_frame, pos_x, pos_y, name_label, health_bar, health_label, action_label, action_bar, target_button, experience_bar, experience_label, y-pos_y))
    print(unit_displays[index])


def generate_bar(frame, bar_value, bar_pos_x, bar_pos_y, bar_style = "green.Horizontal.TProgressbar"):
    bar = ttk.Progressbar(
        frame,
        orient='horizontal',
        mode='determinate',
        length=scale * 6,
        value= bar_value,
        style = bar_style
    )
    bar.grid(column=bar_pos_x, row=bar_pos_y, columnspan=1, padx=scale / 2, pady=scale / 2)
    return bar


def update_bar(bar, bar_value):
    bar.config(value = bar_value)


def generate_label(frame, label_text, label_pos_x = 0, label_pos_y = 0, color = "black"):
    label = tk.Label(frame, font=("Arial", (math.floor(scale / 2))), fg= color)
    label.grid(column = label_pos_x, row = label_pos_y)
    update_label(label, label_text)
    return label

def update_damage_display(fighter_index, damage):
    update_label(unit_displays[i].damage_label, damage_label_text(damage))

def update_label(label, label_text):
    label.config(text = str(label_text))

def update_turn_display(turn):
    turn_label.config(text = turn_label_text(turn))

def update_time_display(runtime):
    update_label(time_label, time_label_text(runtime))

def update_health_display(fighter_index, health, maxhealth):
    i = fighter_index
    update_label(unit_displays[i].health_label, health_label_text(health, maxhealth))
    update_bar(unit_displays[i].health_bar, health_bar_value(health, maxhealth))


def update_action_display(fighter_index, turn, action_start, action_end):
    i = fighter_index
    update_label(unit_displays[i].action_label, action_label_text(turn, action_start, action_end))
    update_bar(unit_displays[i].action_bar, action_bar_value(turn, action_start,action_end))

def update_experience_display(fighter_index, xp, xptolv, owner):
    i = fighter_index
    update_label(unit_displays[i].experience_label, experience_label_text(xp,xptolv, owner))
    update_bar(unit_displays[i].experience_bar, experience_bar_value(xp, xptolv, owner))

def pause_continue():
    global pause
    if pause == True:
        print("fight continues")
        pause_continue_button.config(text ="pause")
        pause = False
    elif pause == False:
        print("Game Paused!")
        pause_continue_button.config(text ="continue")
        pause = True


def move_image(target_frame, source_frame, image_label, desired_column, desired_row):
    # Create a new label in the target frame
    print(f"{target_frame =}, {source_frame=}, {image_label=}, {desired_column=}, {desired_row=}")
    new_image_label = Label(target_frame, image=image_label["image"])
    new_image_label.grid(column=desired_column, row=desired_row)
    # Destroy or hide the original label in the source frame
    image_label.destroy()
    return new_image_label


def on_target_click(new_target_num, old_target_num):
    new_target = new_target_num
    global target
    target = new_target_num
    unit_displays[old_target_num].target_button.config(image = not_target_img)
    unit_displays[new_target_num].target_button.config(image = target_img)

def start_combat():
    combat.mainloop()

def checkpause():
    return pause

def checktarget():
    return target

