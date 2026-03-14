import sqlite3
connnexion = sqlite3.connect("album3.db")#

curseur = connnexion.cursor()
artistes = curseur.execute("SELECT * FROM artiste;").fetchall()
albums = curseur.execute("SELECT * FROM album;").fetchall()# fetchall() permet de récupérer tous les résultats de la requête et de les stocker dans une liste.

for artiste in artistes:
    print(artiste)
    
for album in albums:    
    print(album)    