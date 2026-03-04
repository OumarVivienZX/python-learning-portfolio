#Fichiers texte : Chemins, répertoires et suppression
import os.path


filename = os.path.join ("rep", "mon_fichier.txt")

print(filename ,"\n")
if os.path.exists(filename) :
    print(f"Le fichier {filename} existe .")

    with open(filename,"r") as f :
        contenu = f.read()
        print(contenu)
    f.close()

else :
    print(f"'{filename}' ce fichier n'existe pas")

listdir = os.listdir("rep")
print(listdir)

# os.remove(filename) : supprimer un fichier
# os.rmdir("rep") : supprimer un répertoire (doit être vide)
# os.makedirs("rep") : créer un répertoire (y compris les répertoires parents si nécessaire)
# os.listdir("rep") : lister les fichiers et répertoires dans "rep"
