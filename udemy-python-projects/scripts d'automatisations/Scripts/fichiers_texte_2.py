# EXERCICES : Ecrire les nombres de 1 à 10 dans un fichier texte, chaque nombre sur une ligne différente.
# -----------------------------------------------------------------------------------------------------------------------------------------------------------

with open ("nombre.txt" , "w") as f :
    for i in range(10) : 
        f.write(f" {i+1}\n")

    f.close()

# f = open ("nombre2.txt","w")

# for i in range (10) :
#     f.write(str(i+1) +"\n")

# f.close