#LIRE UN FICHIER TEXTE
#------------------------------------------------------------------------------------------------------------------------------------------------------------
with open ("mon_fichier.txt", "r") as f :
    contenu = f.read() 
    print(contenu, end="")

f.close()

# readline() : lire une ligne du fichier
# readlines() : lire toutes les lignes du fichier et les stocker dans une liste
# read() : lire tout le contenu du fichier et le stocker dans une variable