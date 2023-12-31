import sqlite3


##get_equipment stats does for each slot: get the from the Heroes Table which item_id the Hero has for the respective
##Slot(using getstat), gets the stats for the specific item(using get_item_stats) then applies them(using apply_item_stats)
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


# Usage example:
class Hero():
    def __init__ (self):
        self.name = "testhero"
        self.weapon = 0
        self.chest = 0
        self.hero_id = 0
hero0 = Hero()
hero1 = Hero()
hero2 = Hero()
heroes = [hero0, hero1, hero2]


slots = ["Weapon", "Chest"]  # List all relevant item slots
get_equipment_stats(heroes[0].hero_id, slots)
print("bla")
happy = input("Are you happy?")

print(item[heroes[1].weapon])