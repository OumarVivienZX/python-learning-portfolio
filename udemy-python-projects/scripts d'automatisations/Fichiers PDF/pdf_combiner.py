from PyPDF2 import PdfFileWriter, PdfFileReader  
# Importe les classes nécessaires du module PyPDF2 :
# - PdfFileReader : permet de lire un fichier PDF existant.
# - PdfFileWriter : permet de créer ou modifier un fichier PDF.

# Créer un objet PdfFileWriter (conteneur pour le nouveau PDF).
contenue_sortie = PdfFileWriter()

# Ouvrir les fichiers PDF en mode binaire lecture ("rb").
# "rb" signifie "read binary", indispensable pour manipuler des fichiers PDF.
fichier_pdf_presentation = open("presentation.pdf", "rb")
fichier_pdf_recap = open("recap.pdf", "rb")

# Créer les objets lecteurs pour chaque fichier PDF.
reader_presentation = PdfFileReader(fichier_pdf_presentation)
reader_recap = PdfFileReader(fichier_pdf_recap)

# Afficher le nombre de pages de chaque fichier PDF.
# getNumPages() retourne le nombre total de pages du document.
print("nombre de pages dans le fichier recap =", reader_recap.getNumPages())
print("nombre de pages dans le fichier presentation =", reader_presentation.getNumPages())

# Ajouter la première page du fichier "presentation.pdf".
# getPage(0) retourne la première page (index 0).
contenue_sortie.addPage(reader_presentation.getPage(0))

# Ajouter toutes les pages du fichier "recap.pdf".
# La boucle parcourt chaque page en utilisant son index.
for i in range(reader_recap.getNumPages()):
    contenue_sortie.addPage(reader_recap.getPage(i))

# Écrire le contenu final dans un nouveau fichier PDF.
# "wb" signifie "write binary", nécessaire pour écrire un fichier PDF.
with open("fichier_sortie.pdf", "wb") as fichier_sortie:
    contenue_sortie.write(fichier_sortie)

# Fermer les fichiers ouverts pour libérer les ressources.
fichier_pdf_presentation.close()
fichier_pdf_recap.close()


# 🔑 Classes principales
# - PdfFileReader : pour lire un fichier PDF.
# - PdfFileWriter : pour créer ou modifier un fichier PDF.
# 📖 Méthodes utiles de PdfFileReader
# - getNumPages() → retourne le nombre total de pages.
# - getPage(n) → retourne l’objet PageObject de la page n (index 0‑based).
# - getDocumentInfo() → donne les métadonnées du PDF (titre, auteur, etc.).
# - getPageLayout() / getPageMode() → informations sur l’affichage du PDF.
# ✍️ Méthodes utiles de PdfFileWriter
# - addPage(page) → ajoute une page (objet PageObject).
# - addBlankPage(width, height) → ajoute une page vide.
# - write(file) → écrit le contenu final dans un fichier.
# - cloneDocumentFromReader(reader) → copie toutes les pages d’un PdfFileReader.
