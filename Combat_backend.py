#TODOS:
# Actions improving
# organise Code better
import tkinter as tk
from tkinter import ttk
from tkinter import *
import time
from PIL import Image, ImageTk
import random
from audio import play_sound as sound
import Combat_screen as combatscreen
import math


class Action:
    def __init__(self, name, damage_modifier=1, action_time=100):
        self.name = name
        self.damage_modifier = damage_modifier
        self.action_time = action_time
        self.start_time = 0
        self.finish_time = self.start_time + self.action_time

    def start(self, current_time, source):
        self.start_time = current_time
        self.finish_time = current_time + round((self.action_time * source.attack_time/100))


    def apply(self, source, target):
        damage = source.strength * self.damage_modifier
        target.health -= damage
        print(f"{source.name} uses {self.name} on {target.name} for {damage} damage!")
        combatscreen.cl.log(f"{source.name} uses {self.name} on {target.name} for {damage} damage!")
        sound(target.sounds, "ouch")

def create_attack_action():
    return Action("Attack", damage_modifier=1, action_time=100)

def create_jab_action():
    return Action("Jab", damage_modifier = 0.25, action_time = 30)

def create_slash_action():
    return Action("Slash", damage_modifier=2, action_time=170)

class Unit():
    def __init__(self, name, maxhealth, health, strength, attack_time, sounds = "Default", owner = "computer",
                 index = 0, target_index = 0, actions=[create_attack_action], isalive = True, xp = 0, xptolv = 100, level = 1):
        self.name = name
        self.maxhealth = maxhealth
        self.health = health
        self.strength = strength
        self.attack_time = attack_time
        self.sounds = sounds
        self.owner = owner
        self.target_index = target_index
        self.actions = [action() for action in actions]  # Instantiate new actions
        self.current_action = random.choice(self.actions)
        self.current_action.start(0, self)
        self.isalive = isalive
        self.xp = xp
        self.xptolv = xptolv
        self.level = level
        if(self.owner == "computer"):
            self.xp = round(self.maxhealth * self.strength * 100 / self.attack_time)
        self.index = index

    def perform_action(self, target, current_time):
        self.current_action.apply(self, target)
        combatscreen.update_health_display(target)
        self.current_action = random.choice(self.actions)
        self.current_action.start(current_time, self)



Ada = Unit("Ada", 90, 90, 11, 100, "Ada")
Amy = Unit("Amy", 900, 900, 16, 140, "Amy")
Andi = Unit("Andi", 800, 800, 17, 145, "Andi")
Belen = Unit("Belen", 1000, 1000, 10, 150, "Belen")
big_rat = Unit("Big Rat", 20, 20, 2, 270, )
elite_soldier = Unit("Elite Soldier", 150, 150, 20, 290, )
Erik = Unit("Erik", 90, 90, 11, 100, "Erik")
Lior = Unit("Lior", 95, 95, 12, 560, "Lior")
Luki = Unit("Luki", 1000, 1000, 15, 160, "Luki")
Luna = Unit("Luna", 440, 440, 11, 350, "Luna")
militia = Unit("Militia", 35, 35, 4, 320, )
Paul = Unit("Paul", 1850, 1850, 25, 200, "Paul")
pig = Unit("Pig", 30, 30, 3, 350, "Pig")
rat = Unit("Rat", 10, 10, 1, 140, )
stabber = Unit("Stabber", 25, 25, 25, 205, )
soldier = Unit("Soldier", 60, 60, 6, 310, )
swordsman = Unit("Swordsman", 80, 80, 8, 300, actions = [create_slash_action, create_attack_action])

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
fighters[0].target_index = 1
fighters.append(Luki)
fighters.append(Andi)
fighters.append(swordsman)
fighters.append(pig)
fighters[4].target_index = 2


i = 0
for fighter in fighters:
    fighter.index = i
    i += 1


global turn
turn = 0
global pause_combat
pause_combat = True


def combatevent(fighter, turn):
    if fighter.owner == "player":
        fighter.target_index = combatscreen.checktarget()
    defender_number = fighter.target_index
    defender = fighters[defender_number]
    fighter.perform_action(defender, turn)
    if defender.isalive == False:
        sound("Default", "hit dead one")
    if defender.health <= 0 and defender.isalive == True:
        sound(fighters[defender_number].sounds, "death")
        defender.isalive = False
        defender.action = "none"
        combatscreen.update_action_display(defender, turn)
        defender.health = 0
        try:
            combatscreen.cl.log(f"{defender.name} Died")
        except:
            print("couldnt print death message to combatlog")
        combatscreen.update_health_display(defender)
        if(fighter.owner == "player"):
            fighter.xp = fighter.xp + defender.xp
            combatscreen.update_experience_display(fighter.index, fighter.xp, fighter.xptolv, fighter.owner)
            try:
                combatscreen.cl.log(f"{fighter.name} gained {defender.xp} experience")
            except:
                print("couldnt print experience gained to combat log")
            while(fighter.xp > fighter.xptolv):
                fighter.xp = fighter.xp - fighter.xptolv
                fighter.level = fighter.level + 1
                fighter.attacktime = math.floor(fighter.attack_time * 0.9)
                fighter.xptolv = fighter.xptolv + (100 * fighter.level)
                try:
                    combatscreen.cl.log(f"{fighter.name} is now level {fighter.level}")
                except:
                    print("coulnt print levelup message to combat log")
                try:
                    combatscreen.combat.after(250,sound(fighter.sounds, "levelup"))
                except:
                    print("couldnt play levelup sound")
                try:
                    combatscreen.update_experience_display(num, fighter.xp, fighter.xptolv, fighter.owner )
                except:
                    print("experience display couldnt be updated")

Print("testest")
def combattime():
    combat = True
    global pause_combat
    global turn

    for fighter in fighters:
        if fighter.isalive == True:
            if fighter.current_action.finish_time == turn:
                combatevent(fighter, turn)
            combatscreen.update_action_display(fighter, turn)
    i = 0
    combatscreen.update_turn_display(turn)
    turn = turn + 1
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