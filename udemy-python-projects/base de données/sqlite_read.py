import sqlite3
con = sqlite3.connect("album3.db")

curseur = con.cursor()
artistes = curseur.execute("SELECT * FROM artiste;").fetchall()
albums = curseur.execute("SELECT * FROM album;").fetchall()

for artiste in artistes:
    print(artiste)
    
for album in albums:    
    print(album)    