import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter import *
import time
from PIL import Image, ImageTk
import random
from audio import play_sound as sound

# Create instance
parent = tk.Tk()
scale = 20
parentsize = str(scale * 60) + "x" + str(scale * 30)
parent.geometry(parentsize)
# Add a title
parent.title("fightwindow")





class Unit():
    def __init__(self, name, maxhealth, health, damage, attacktime,sounds, owner = "Computer", target = 0):
        self.name = name
        self.maxhealth = maxhealth
        self.health = health
        self.damage = damage
        self.attacktime = attacktime
        self.sounds = sounds
        self.owner = owner
        self.target = target



rat = Unit("Rat", 10, 10, 1,1400, "Default")
big_rat = Unit ("Big Rat", 20, 20, 2, 2700, "Default")
militia = Unit("Militia", 35, 35, 4, 3200, "Default")
soldier = Unit( "Soldier", 60, 60, 6, 3100, "Default")
pig = Unit("Pig", 30, 30, 3, 3500, "Pig")
Lior = Unit("Lior", 95, 95, 12, 5600, "Lior")
Luki = Unit( "Luki", 1000, 1000, 15, 6500, "Luki")
Luna = Unit("Luna", 440,440,11, 3500, "Luna")
Belen = Unit("Belen", 2000, 1000, 10, 4500, "Belen")
Ada = Unit("Ada", 9000, 9000, 11, 1000, "Ada")
Mila = Unit("Mila", 9000, 9000, 11, 1000, "Mila")



fighters = []
fighters.append(Mila)
fighters.append(Lior)
fighters.append(Luna)
fighters.append(soldier)
fighters.append(Luki)

fighters[0].target = 1
fighters[0].owner = "Player"

combatants = (len(fighters))
name_labels = []
health_bars = []
health_labels = []
damage_labels = []
attacktime_labels = []
action_bars = []
target_buttons = []


actions = []
actions_start = []
actions_end = []

global turn
turn = 0
global pause_combat
pause_combat = True

def update_health_display(num):
    health_labels[num].config(text = "Health: " + str(fighters[num].health) + "/" + str(fighters[num].maxhealth))
    health_bars[num]['value'] = fighters[num].health / fighters[num].maxhealth * 100

def update_action_bar(num,turn):
    action_bars[num]['value'] = (turn - actions_start[num]) /(actions_end[num] - actions_start[num]) * 100
    print("Turn: " + str(turn) + " actions_start[num]" + str(actions_start[num]) + " actions_end[num]" + str(actions_end[num]))
    if fighters[num].isalive == False:
        action_bars[num]['value'] = 0


def on_fight_click():
    print("fight clicked")
    global pause_combat
    pause = False
    parent.after(10, combattime())

def on_stop_click():
    print("stop clicked")
    global pause_combat
    pause = True

img = Image.open("pictures/Target.jpg")
image1 = ImageTk.PhotoImage(img)
target_sign = Label(parent, image = image1)
def on_target_click(num):

    target_sign.grid(column = num, row = 7)
    fighters[0].target = num
    print("New Target = " + str(fighters[0].target))


for num in range(combatants): ## Initialization of participants
    fighters[num].isalive = True
    name_label = tk.Label(parent, text =  fighters[num].name, font = ("Arial", scale), fg = "Black")
    name_label.grid(column = num, row = 0)
    rows_used = 0
    # health_bars
    health_bars.append(ttk.Progressbar(
        parent,
        orient='horizontal',
        mode='determinate',
        length=150,
        value = 100
    ))
    # place the health_bars
    rows_used += 1
    health_bars[num].grid(column=num, row=rows_used, columnspan=1, padx=10, pady=10)

    health_labels.append(tk.Label(parent, text = "Health: " + str(fighters[num].health), font = ("Arial", 10,), fg = "red"))
    rows_used += 1
    health_labels[num].grid(column = num, row = rows_used)

    damage_labels.append(tk.Label(parent, text = "Damage: " + str(fighters[num].damage), font = ("Arial", 10,), fg = "brown"))
    rows_used += 1
    damage_labels[num].grid(column = num, row = rows_used)

    attacktime_labels.append(tk.Label(parent, text = "Attacktime: " + str(fighters[num].attacktime/1000) + " seconds" , font = ("Arial", 10,), fg = "brown"))
    rows_used += 1
    attacktime_labels[num].grid(column = num, row = rows_used)

    # actionbars
    action_bars.append(ttk.Progressbar(
        parent,
        orient='horizontal',
        mode='determinate',
        length=100,
        value = 0,
    ))
    rows_used += 1
    action_bars[num].grid(column=num, row=rows_used, columnspan=1, padx=10, pady=10)
    actions.append("Attack")
    actions_start.append(turn)
    actions_end.append(turn + fighters[num].attacktime)
    rows_used += 1
    target_buttons.append(tk.Button(parent, text="Make target", command=lambda n = num: on_target_click(n)))
    target_buttons[num].grid(column = num, row = rows_used)


def combatloop(turn):
    print("combatloop entered")
    for num in range(combatants):
        if actions_end[num] == turn:
            targetnum = fighters[num].target
            if(actions[num] == "Attack"):
                fighters[targetnum].health = fighters[targetnum].health - fighters[num].damage
                update_health_display(targetnum)
                if(random.random() < 0.1):
                    fighters[targetnum].health = fighters[targetnum].health - (fighters[num].damage)
                    update_health_display(targetnum)
                    sound(fighters[num].sounds, "yay")
                else:
                    sound(fighters[targetnum].sounds, "ouch")



                if fighters[num].owner == "Computer":
                    actions_end[num] = turn + fighters[num].attacktime
                    actions_start[num] = turn
                    update_action_bar(num, turn)
                if fighters[num].owner == "Player":
                    actions_end[num] = turn + fighters[num].attacktime
                    actions_start[num] = turn
                    update_action_bar(num, turn)
            if fighters[targetnum].health <= 0 and fighters[targetnum].isalive == True:
                showinfo(message = fighters[targetnum].name + " Died")
                sound(fighters[targetnum].sounds, "death")
                fighters[targetnum].isalive = False
                actions[targetnum] = "none"
                on_stop_click()


def combattime():
    combat = True
    global pause_combat
    global turn
    turn = turn + 1
    parent.update
    combatloop(turn)
    if pause == False:
        parent.after(1, combattime)
    for num in range(combatants):
        update_action_bar(num, turn)




pause_continue_button = tk.Button(parent, text ="Fight", command =on_fight_click)
rows_used += 1
pause_continue_button.grid(column = 0, row = rows_used)
stop_button = tk.Button(parent, text = "Stop", command =on_stop_click)
rows_used += 1
stop_button.grid(column = 0, row = rows_used)
# Start GUI
parent.mainloop()



