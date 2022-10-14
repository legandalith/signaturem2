import mysql.connector
import sqlite3
import time
from PIL import Image, ImageDraw, ImageFont
import sqlite3
import time

db = mysql.connector.connect(
    host = "192.168.1.41",
    user = "root",
    password = "123456789",
    database = ""
)

myc = db.cursor()

def foto():
    vt = sqlite3.connect('player.db')
    im = vt.cursor()
    satir = im.execute('SELECT COUNT (id) FROM player')
    satirx = im.fetchone()
    font = ImageFont.truetype("fonts/Tibia.ttf", 18)
    img = Image.open("bg/background.jpg")
    draw = ImageDraw.Draw(img)
    start = 1
    while start <= satirx[0]:
        img = Image.open("bg/background.jpg")
        draw = ImageDraw.Draw(img)
        im.execute('SELECT name, level, playtime from player WHERE id={}'.format(start))
        resultx = im.fetchall()
        mn = 0
        draw.text((40,40), str(resultx[mn][0]), font=font, fill="red")
        draw.text((40,60), str(resultx[mn][1]), font=font, fill="blue")
        draw.text((40,80), str(resultx[mn][2]), font=font, fill="green")
        img.save("image/{}.png".format(start))
        start+=1
        while mn <= satirx[0]:
            mn+=1

while True:
    myc.execute("SELECT id, name, level, playtime FROM player.player")
    result = myc.fetchall()
    kactane = len(result)
    n = 0
    while n <= kactane:
        a = result[n][0]
        b = result[n][1]
        c = result[n][2]
        d = result[n][3]
        vt = sqlite3.connect('player.db')
        im = vt.cursor()
        im.execute('INSERT INTO player VALUES ((?),(?),(?),(?))',(a,b,c,d))
        n+=1
        vt.commit()
        foto()
        if n == kactane:
            time.sleep(10)
            im.execute('DELETE FROM player')
            vt.commit()
            break