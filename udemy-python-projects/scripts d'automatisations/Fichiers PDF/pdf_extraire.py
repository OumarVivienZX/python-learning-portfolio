from PyPDF2 import PdfFileReader,PdfFileWriter

fichier = open("recap.pdf","rb")

reader_fichier = PdfFileReader(fichier)

Page0 = reader_fichier.getPage(0)
texte = Page0.extractText()
texte = texte.replace("Ò" , '"').replace("‹" , 'à').replace('”' , "é").replace("Õ" , "'")

fichier.close()

print(texte)