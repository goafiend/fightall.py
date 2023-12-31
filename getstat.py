import sqlite3
db = "game.db"
conn = sqlite3.connect(db)
def getstat(table, id, stat):
    query =(f"select {stat} from {table} where id = {id}")
    cursor = conn.execute(query)
    result = cursor.fetchone()[0]
    print(result)

table = input("Which Table do you want to query?")
id = input("which id do you want to query?")
stat = input("which Stat do you want to query?")
getstat(table,id,stat)