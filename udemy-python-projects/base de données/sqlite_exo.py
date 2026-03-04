import sqlite3

con = sqlite3.connect("album3.db")

curseur = con.cursor()

curseur.execute("""CREATE TABLE artiste (
    artiste_id INTEGER NOT NULL PRIMARY KEY, 
    nom VARCHAR);""")

curseur.execute("""CREATE TABLE album (
    album_id INTEGER NOT NULL PRIMARY KEY, 
    artiste_id INTEGER REFERENCES artiste,
    titre VARCHAR,
    annee_sortie INTEGER);""")

curseur.execute("INSERT INTO artiste (nom) VALUES ('Michael Jackson');")
MJ_id = curseur.lastrowid
curseur.execute("INSERT INTO artiste (nom) VALUES ('Celine Dion');")
CD_id = curseur.lastrowid

curseur.execute("INSERT INTO album (artiste_id, titre, annee_sortie) VALUES (?, 'Thriller', 1982);", (MJ_id,))#cette syntaxe permet d'insérer des données de manière sécurisée en utilisant des paramètres de requête, ce qui évite les risques d'injection SQL.
curseur.execute("INSERT INTO album (artiste_id, titre, annee_sortie) VALUES (?, 'La Voix du Bon Dieu', 1981);", (CD_id,))#cette syntaxe permet d'insérer des données de manière sécurisée en utilisant des paramètres de requête, ce qui évite les risques d'injection SQL.

con.commit()
con.close()