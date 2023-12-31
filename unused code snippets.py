for equip in self.equipment:
    critchance += equip.critchance
    ias += equip.ias
    attack += equip.attack
    constitution += equip.constitution
    armor += equip.armor

    def getequipment(self): ## NOT WORKING getting Equipment
        for i in range(0, 11): ##initializing the equipped variable
            self.equipment.append(Item)
            self.equipment[i].empty = True
        self.weapon = getstat("Heroes", self.heroid, "weapon")
        getitem(weapon, 0, self.weapon, 0)
        self.chest = getstat("Heroes", self.heroid, "chest")
        getitem(chest, 0, self.chest, 0)

class Item:
    name = "needsname"
    slot = "needslot"
#equppement in slots is an array: 1 = hand1, 2 = hand2, 3 = Head, 4 = neck, 5 = chest, 6 = Gloves, 7 = Belt, 8= Boots
#9 = ring 1 10 = ring2. the characters base stats are in 0

def getitem(whereto, target, id, suffix): ##  NOT WORKING Getting all stats of a Specific Item, whereto points where it should be put
    db = "game.db"
    conn = sqlite3.connect(db)
    print("accessing the database ", db)
    character[target].equipped[slot].empty = False
    character[target].equipped[slot].name = getstat("items", id, "name")
    print("name: ", character[target].equipped[slot].name, " of target: ", target, " in slot ", slot)
    character[target].equipped[slot].attack = getstat("items", id, "attack")
    character[target].equipped[slot].armor = getstat("items", id, "armor")
    character[target].equipped[slot].attackspeed = getstat("items", id, "attackspeed")
    character[target].equipped[slot].critchance = getstat("items", id, "critchance")
    character[target].equipped[slot].strength = getstat("items", id, "strength")
    character[target].equipped[slot].constitution = getstat("items", id, "constitution")
    character[target].equipped[slot].intelligence = getstat("items", id, "intelligence")
    character[target].equipped[slot].wisdom = getstat("items", id, "wisdom")
    character[target].equipped[slot].block = getstat("items", id, "block")
    character[target].equipped[slot].blockchance = getstat("items", id, "blockchance")
    character[target].equipped[slot].ias = getstat("items", id, "ias")
    character[target].equipped[slot].defense = getstat("items", id, "defense")