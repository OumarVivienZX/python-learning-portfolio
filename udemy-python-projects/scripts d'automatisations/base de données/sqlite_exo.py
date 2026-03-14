import sqlite3  # Importe le module sqlite3, qui permet de manipuler des bases de données SQLite en Python.

# Connexion à la base de données "album3.db". 
# Si le fichier n'existe pas, SQLite le crée automatiquement.
con = sqlite3.connect("album3.db")

# Création d’un objet curseur, utilisé pour exécuter des requêtes SQL sur la base.
curseur = con.cursor()

# Création de la table "artiste" avec deux colonnes :
# - artiste_id : identifiant unique, entier, obligatoire (NOT NULL), clé primaire (PRIMARY KEY).
# - nom : chaîne de caractères (VARCHAR).
curseur.execute("""CREATE TABLE artiste (
    artiste_id INTEGER NOT NULL PRIMARY KEY, 
    nom VARCHAR);""")

# Création de la table "album" avec quatre colonnes :
# - album_id : identifiant unique, entier, obligatoire, clé primaire.
# - artiste_id : entier, clé étrangère (REFERENCES artiste) qui relie chaque album à un artiste.
# - titre : chaîne de caractères (VARCHAR).
# - annee_sortie : entier représentant l’année de sortie de l’album.
curseur.execute("""CREATE TABLE album (
    album_id INTEGER NOT NULL PRIMARY KEY, 
    artiste_id INTEGER REFERENCES artiste,
    titre VARCHAR,
    annee_sortie INTEGER);""")

# Insertion d’un nouvel artiste dans la table "artiste".
curseur.execute("INSERT INTO artiste (nom) VALUES ('Michael Jackson');")
# Récupération de l’ID automatiquement généré pour Michael Jackson.
MJ_id = curseur.lastrowid

# Insertion d’un autre artiste.
curseur.execute("INSERT INTO artiste (nom) VALUES ('Celine Dion');")
# Récupération de l’ID automatiquement généré pour Céline Dion.
CD_id = curseur.lastrowid

# Insertion d’un album lié à Michael Jackson.
# Le "?" est un paramètre de requête : il sera remplacé par la valeur de MJ_id.
# Cette méthode est sécurisée car elle évite les injections SQL.
curseur.execute("INSERT INTO album (artiste_id, titre, annee_sortie) VALUES (?, 'Thriller', 1982);", (MJ_id,))

# Insertion d’un album lié à Céline Dion.
# Même principe : le "?" est remplacé par CD_id.
curseur.execute("INSERT INTO album (artiste_id, titre, annee_sortie) VALUES (?, 'La Voix du Bon Dieu', 1981);", (CD_id,))

# Validation des modifications (INSERT et CREATE TABLE).
con.commit()

# Fermeture de la connexion à la base de données.
con.close()