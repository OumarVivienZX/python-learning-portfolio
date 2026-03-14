# Gestion des erreurs
import os

filename = "mon_fichier.txt"

if os.path.exists(filename) :
    print(f"Le fichier {filename} existe .")

    with open(filename,"r") as f :
        contenu = f.read()
        print(contenu)
    f.close()

else :
    print(f"'{filename}' ce fichier n'existe pas")

# filename = "mon_fichier.txt"
# try :
#     f = open(filename, "r")

# except FileNotFoundError :
#     print("Le fichier spécifié n'existe pas")

# else :
#     contenu = f.read()
#     print(contenu)
#     f.close()