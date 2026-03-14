import zipfile
import shutil
# fichier_zipé = zipfile.ZipFile("Résumé_des_ventes.zip", "w", zipfile.ZIP_DEFLATED)

# fichier_zipé.write("Octobre.xlsx")
# fichier_zipé.write("Novembre.xlsx")
# fichier_zipé.write("Decembre.xlsx")
# fichier_zipé.close()
shutil.make_archive("Résumé_des_ventes2", "zip", "Résumé_des_ventes")# make_archive() est une fonction de la bibliothèque shutil qui permet de créer une archive compressée. Les arguments sont :
# - "Résumé_des_ventes2" : le nom de l'archive sans l'extension .zip.
# - "zip" : le format de compression, ici ZIP. 
# - "Résumé_des_ventes" : le répertoire à compresser, qui contient les fichiers Excel à inclure dans l'archive.
shutil.unpack_archive("Résumé_des_ventes2.zip", "Résumé_des_ventes_decompressé")# unpack_archive() est une fonction de la bibliothèque shutil qui permet de décompresser une archive. Les arguments sont :
# - "Résumé_des_ventes2.zip" : le nom de l'archive à