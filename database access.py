import sqlite3
connection = sqlite3.connect("game.db")
cursor = connection.execute("select * from Heroes")
names = [description[0] for description in cursor.description]
print(names)
cursor = connection.execute("select * from Heroes")
Heroes = cursor.fetchall()
for hero in Heroes:
    for column in hero:
        i = hero.index(column)
        print(names[i], ": ", column)
cursor = connection.execute("select name from items where id = 1")
weaponname = cursor.fetchone()
cursor = connection.execute("select attack from items where id = 1")
weaponattack = cursor.fetchone()
print(weaponname)


connection.close()