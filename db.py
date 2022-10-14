import sqlite3

con = sqlite3.connect("player.db")

cursor = con.cursor()

def create_tab():
    cursor.execute("""CREATE TABLE IF NOT EXISTS player (id, name, level, playtime)""")
    con.commit()
create_tab()
con.close()