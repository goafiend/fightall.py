#TODOS:
# Actions


import tkinter as tk
from tkinter import ttk
from tkinter import *
import time
from PIL import Image, ImageTk
import random
from audio import play_sound as sound
import Demo_Paul_Combatscreen as combatscreen
import math





class Unit():
    def __init__(self, name, maxhealth, health, damage, attacktime, sounds = "Default", owner = "computer",
                 target = 0, action = "attack", action_start = 0, isalive = True, xp = 0, xptolv = 100, level = 1):
        self.name = name
        self.maxhealth = maxhealth
        self.health = health
        self.damage = damage
        self.attacktime = attacktime
        self.sounds = sounds
        self.owner = owner
        self.target = target
        self.action = action
        self.action_start = action_start
        self.action_end = self.action_start + self.attacktime
        self.isalive = isalive
        self.xp = xp
        self.xptolv = xptolv
        self.level = level
        if(self.owner == "computer"):
            self.xp = self.maxhealth * self.damage * 100 /self.attacktime
    def clone(self):
        # Create a new instance with the same initial attributes
        return Unit(
            self.name,
            self.maxhealth,
            self.maxhealth,  # Set initial health to maxhealth
            self.damage,
            self.attacktime,
            self.sounds,
            self.owner,
            self.target,
            self.action,
            self.action_start,
            self.isalive,
            self.xp,
            self.xptolv,
            self.level
        )


Ada = Unit("Ada", 90, 90, 11, 100, "Ada")
Amy = Unit("Amy", 900, 900, 16, 140, "Amy")
Andi = Unit("Andi", 800, 800, 17,145, "Andi")
Belen = Unit("Belen", 1000, 1000, 10, 150, "Belen")
big_rat = Unit ("Big Rat", 20, 20, 2, 270)
elite_soldier = Unit("Elite Soldier", 150,150,20,290)
Erik = Unit("Erik", 90, 90, 11, 100, "Erik")
Lior = Unit("Lior", 95, 95, 12, 560, "Lior")
Luki = Unit( "Luki", 1000, 1000, 15, 160, "Luki")
Luna = Unit("Luna", 440,440,11, 350, "Luna")
militia = Unit("Militia", 35, 35, 4, 320)
Paul = Unit("Paul", 1850, 1850, 25, 200, "Paul")
pig = Unit("Pig", 30, 30, 3, 350, "Pig")
rat = Unit("Rat", 10, 10, 1,140)
stabber = Unit("Stabber", 25, 25, 25, 205)
soldier = Unit( "Soldier", 60, 60, 6, 310)
swordsman = Unit("Swordsman", 80, 80, 8, 300)

# low_units = [soldier, militia, swordsman, stabber]
# def generate_enemy(unit_tier, num):
#     if unit_tier == 1:
#         fighters.pop(num)
#         fighter = random.choice(low_units)
#         fighter.action_start = turn
#         fighter.action_end = turn + fighter.attacktime
#         fighters.insert(num, fighter)
#         fighters[num].isalive = True
#         combatscreen.update_combatant(fighters[num], num)



fighters = []
fighters.append(Paul)
fighters[0].xp = 0
fighters[0].owner = "player"
fighters[0].target = 1
fighters.append(Luki)
fighters.append(Andi)
soldier2 = soldier.clone()
fighters.append(soldier2)
fighters.append(stabber)
fighters.append(Ada)
global turn
turn = 0
global pause_combat
pause_combat = True


def combatloop(turn):
    fighters_number = len(fighters)
    for num in range(fighters_number):
        if fighters[num].action_end == turn:
            attacker = fighters[num]
            if attacker.owner == "player":
                attacker.target = combatscreen.checktarget()
            defender_number = attacker.target
            defender = fighters[defender_number]
            if(attacker.action == "attack" and defender.isalive == True):

                if(random.random() < 0.1):
                    defender.health = defender.health - (attacker.damage *2)
                    sound(fighters[num].sounds, "yay")
                    try:
                        combatscreen.cl.log(f"{attacker.name} hit {defender.name} critical for {attacker.damage*2}")
                    except:
                        print("couldnt output crit to combatlog")
                else:
                    defender.health = defender.health - attacker.damage
                    sound(fighters[defender_number].sounds, "ouch")
                    try:
                        combatscreen.cl.log(f"{attacker.name} hit {defender.name} for {attacker.damage}")
                    except:
                        print("couldnt output hit to combat")
                combatscreen.update_health_display(defender_number, defender.health, defender.maxhealth)
            attacker.action_end = turn + attacker.attacktime
            attacker.action_start = turn
            if (fighters[num].action == "attack" and defender.isalive == False):
                sound("Default", "hit dead one")
            if defender.health <= 0 and defender.isalive == True:
                sound(fighters[defender_number].sounds, "death")
                defender.isalive = False
                defender.action = "none"
                combatscreen.update_action_display(defender_number, turn, 1, 3)
                defender.health = 0
                try:
                    combatscreen.cl.log(f"{defender.name} Died")
                except:
                    print("couldnt print death message to combatlog")

                combatscreen.update_health_display(defender_number, defender.health, defender.maxhealth)
                if(attacker.owner == "player"):
                    attacker.xp = attacker.xp + defender.xp
                    combatscreen.update_experience_display(num, attacker.xp, attacker.xptolv, attacker.owner)
                    try:
                        combatscreen.cl.log(f"{attacker.name} gained {defender.xp} experience")
                    except:
                        print("couldnt print experience gained to combat log")
                    # generate_enemy(1, defender_number)
                    while(attacker.xp > attacker.xptolv):
                        attacker.xp = attacker.xp - attacker.xptolv
                        attacker.level = attacker.level + 1
                        attacker.attacktime = math.floor(attacker.attacktime * 0.89)
                        attacker.xptolv = attacker.xptolv + (100 * attacker.level)
                        try:
                            combatscreen.cl.log(f"{attacker.name} is now level {attacker.level}")
                            combatscreen.cl.log(f"{attacker.name} now has increased attackspeed. new attacktime: {attacker.attacktime} turns")
                        except:
                            print("coulnt print levelup message to combat log")
                        try:
                            combatscreen.combat.after(50,sound(attacker.sounds, "levelup"))
                        except:
                            print("couldnt play levelup sound")
                        try:
                            combatscreen.update_experience_display(num, attacker.xp, attacker.xptolv, attacker.owner )
                        except:
                            print("experience display couldnt be updated")


def combattime():
    combat = True
    global pause_combat
    global turn
    turn = turn + 1

    combatloop(turn)
    i = 0
    combatscreen.update_turn_display(turn)
    for fighter in fighters:
        if fighter.isalive == True:
            combatscreen.update_action_display(i, turn, fighter.action_start, fighter.action_end)

        i += 1

st = time.time()
def game_time():
    pause = combatscreen.checkpause()
    global st
    runtime = time.time() - st
    combatscreen.update_time_display(runtime)
    if (pause == False):
        combattime()
    combatscreen.combat.after(10, game_time)

combatscreen.generate_combat_window(fighters)

game_time()

combatscreen.start_combat()