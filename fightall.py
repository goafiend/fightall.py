import math
import random
import time
import os
import sqlite3
log = True
db = "game.db"
conn = sqlite3.connect(db)
print("accessing the database ", db)
conn.close()
possibleperks = 6

##TODOS:
##Item System Remake needs to be Finished. until then no Items.
##update herogen function and create unitgen function
##change perks to database



def get_equipment_stats(Hero_id, slots): ## gets the stats for all equipment of a Hero
    for slot in slots:
        print("Slot: ", slot)
        slotname = slot
        item_id = getstat("Heroes", Hero_id, slot)
        item_stats = get_item_stats(slotname, item_id)


def get_item_stats(slot, item_id):
    item_stats = []
    item_table = slot + "s"
    attributes = get_item_attributes(slot, item_id)
    for attribute in attributes:
        value = getstat(item_table, item_id, attribute)


def get_item_attributes(slot, item_id):
    db = "game.db"
    conn = sqlite3.connect(db)
    table = slot + "s"
    cursor = conn.execute(f"SELECT * FROM {table} WHERE id = {item_id}")
    row = cursor.fetchone()
    columns = [column[0] for column in cursor.description]

    conn.close()
    return columns

def getstat(table, id, stat):  ##getting specific stat from db, returned as result
    db = "game.db"
    conn = sqlite3.connect(db)
    query = f"select {stat} from {table} where id = {id}"
    cursor = conn.execute(query)
    result = cursor.fetchone()[0]

    conn.close()
    return result


class Unit:
    race = "none"
    ap1000 = 0
    armor = 0
    attack = 0
    attackspeed = 4
    block = 0
    blockchance = 0
    critchance = 0
    critdmg = 0
    defense = 0
    dmgr = 0
    goldreward = 0
    hp = 0
    ias = 0
    maxhp = 0
    mindmg = 0
    nturn = 0
    owner = "none"
    xpreward = 0
    perks = []



class Player:
    gold = 0
    perks = []


class Hero(Unit):

    equipment = []
    equipment.append("Weapon")
    equipment.append("Chest")

    level = 0
    xptonextlv = 100
    heroid = 0
    availableperks = possibleperks
    def statscalc(self):


        if "Swiftness" in self.perks:
            ias += perk[1].value1
            critchance = 0
            ap1000 = round((1 + ias/100) * self.attackspeed)
            maxhp = constitution * 10
            mindmg = attack * 0.75 * (1 + strength/10)
            dmgr = attack * 1.25 * (1 + strength/10)
        if "Critical Strikes" in self.perks:
                critchance += perk[0].value1
                critdmg += perk[0].value2
        if "Resilience" in self.perks:
                armor = armor * (1 + (perk[2].value1 / 100)) + perk[2].value2
        if "Unreliable Damage" in self.perks:
                dmgr += (mindmg * (1 + (perk[4].value1 / 100)))





    def lvlup(self):
        level += 1
        xptonextlevel = 100 + character[attacker].xptonextlv * 1.15
        print("congratulations", self.name, " reached level ", self.level)
        option = []
        a = 1
        while a < 3:
            i = (round(random.uniform(0, 5)))
            if i not in option and perk[i].name not in character[attacker].perks:
                option.append(i)

                print(perk[option[a]].name, "[", a, "]")
                print(perk[option[a]].description)
                a = a + 1
                if (a >(self.availableperks - self.perks.len())):
                    print("no more perks to learn")

        choice = int(input("Choose a perk to learn:"))
        print(perk[option[a]].name)
        character[attacker].perks.append(perk[option[a]].name)
        print("Perks:", character[attacker].perks)

class Item():
    def __init__(self):
        self.name = "noname"
        self.type = "notype"
        self.value = 0

class Weapon(Item):
    def __init__(self):
        self.type = "Weapon"
        self.attack = 0
        self.attackspeed = 5
class Chest(Item):
    def __init__(self):
        self.type = "Chest"
        self.armor = 0
        self.block = 0

character = []

def herogen():  #generates the player character NO EQUIPMENT UNTIL ITS REWORKED

    character.append(Hero())

    character[0].owner = "player"
    heroid = 0

    get_equipment_stats(0, ["Weapon", "Chest"])
    character[0].name = input("whats your Name?")
    character[0].xp = getstat("Heroes", heroid, "xp")
    character[0].gold = getstat("heroes", heroid, "gold")
    character[0].lv = getstat("heroes", heroid, "lv")

herogen()
print(character[0].name)
print(vars(character[0]))
a = input("?")

def unitgen():
    newunit = Unit()


def perksgen():


    class Perk:
        Name = "noname"
    a = 0
    while a < possibleperks:
        perk.append(Perk())
        a += 1
    perk[0].name = "Critical Strikes"
    perk[0].value1 = 5
    perk[0].value2 = 100
    perk[0].description = "You have a ", perk[0].value1, "% chance to deal ", perk[0].value2, "% more strength with an attack"

    perk[1].name = "Swiftness"
    perk[1].value1 = 10
    perk[1].description = " increases attack speed by", perk[1].value1, "%"

    perk[2].name = "Resilience"
    perk[2].value1 = 5
    perk[2].value2 = 0.2
    perk[2].description = "increases Armor by ", perk[2].value1, "% + ", perk[2].value2, " per character level"

    perk[3].name = "destroy Armor"
    perk[3].value1 = 2
    perk[3].description = "attacks reduce the Target's armor by ", perk[3].value1, "% of the attack strength before Armor"

    perk[4].name = "Unreliable Damage"
    perk[4].value1 = 30
    perk[4].description = "adds ", perk[4].value1, " percent of your minimal strength to your strength range"
    
    perk[5].name = "Smart"
    perk[5].value1 = 15
    perk[5].value2 = 10
    perk[5].description = ("You get ", perk[5].value1, " Percent more Gold and ", perk[5].value2, " Percent more xp")


def menu():
    global play
    print(play)
    while play:
        character[0].statscalc()
        healamount = (character[0].maxhp - character[0].hp)
        healcost = healamount * 5
        print(f" what would you like to do? fight or exit? make enemies stronger(stronger), heal(costs {healcost} gold to heal {healamount} Health)?, show stats?")
        choice = input(":")
        if choice == "fight":
            encounterspawn(1)
            fight()
        elif choice == "stronger":
            global difficulty
            difficulty += 1
        elif choice == "exit":
            print("thanks for playing")
            play = False
        elif choice == "heal":
            character[0].hp = character[0].maxhp
            character[0].gold -= healcost
            print("you were healed")
        elif choice == "stats":
            stats()


def stats():
    print(f"health: {character[0].hp} of {character[0].maxhp} Attackspeed: {character[0].ap1000} /1000, Armor: {character[0].armor}, strength: {character[0].mindmg} - {character[0].dmgr + character[0].mindmg}")
    print(f"Level: {character[0].lv} Experience: {character[0].xp} of {character[0].xptonextlv} Gold: {character[0].gold} ")
    print(f"Perks: {character[0].perks}")


def fight():
    turn = 0
    fighters = 2
    a = 0
    while a < fighters:
        character[a].nturn = round(turn + 1000 / character[a].ap1000)
        a = a + 1

    while character[0].hp > 0 and character[1].hp > 0:
        waiting = ((min(character[0].nturn, character[1].nturn)) - turn) / 100
        print(waiting)
        time.sleep(waiting)
        turn = min(character[0].nturn, character[1].nturn)
        print("turn: ", turn)
        if character[0].nturn == turn:
            attacker = 0
            defender = 1
        if character[1].nturn == turn:
            attacker = 1
            defender = 0
        hit = round(character[attacker].mindmg + random.uniform(0, character[attacker].dmgr) - character[defender].armor)
        if character[attacker].critchance > 0:
            critroll = random.randint(0, 100)
            if critroll < character[attacker].critchance:
                hit *= 1 + (character[attacker].critdmg/100)

        print(character[attacker].name, " hits ", character[defender].name, " for ", hit, "strength points")
        character[defender].hp -= hit
        character[attacker].nturn += round(1000/character[attacker].ap1000)

    if character[0].hp < 1:
        print("you die, suckeer! ")
        time.sleep(2)
        global play
        play = False

    if character[1].hp < 1:
        if "Smart" in character[attacker].perks:
            character[defender].goldreward = character[defender].goldreward * (perk[5].value1 + 100)/100
            character[defender].xpreward = character[defender].xpreward * (perk[5].value1 + 100)/100

        print("you killed ", character[defender].name)
        character[attacker].xp = character[attacker].xp + character[defender].xpreward
        print("you get", character[defender].xpreward, "Experience, now you have ", character[attacker].xp, " / ", character[attacker].xptonextlv, "Experience")
        character[attacker].gold = character[attacker].gold + character[defender].goldreward
        print("you get ", character[defender].goldreward, " Gold. now you have ", character[attacker].gold)
        character.pop(defender)

        if character[attacker].xp >= character[attacker].xptonextlv:
            lvlup(attacker)


play = True
difficulty = 1
character = []

perk = []
perksgen()
herogen()
menu()
