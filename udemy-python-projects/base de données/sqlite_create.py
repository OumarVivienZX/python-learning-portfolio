import sqlite3

# Créer ou ouvrir la base de données
con = sqlite3.connect("album2.db")

# Définir la commande SQL
sql__table_artiste = """
CREATE TABLE artiste (
    artiste_id INTEGER NOT NULL PRIMARY KEY,
    nom VARCHAR
);
"""

# Créer un curseur
curseur = con.cursor()

# Exécuter la commande
curseur.execute(sql__table_artiste)

# Sauvegarder
con.commit()

# Fermer la connexion
con.close()