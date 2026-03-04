# # def demander_mot_de_passe(mot_de_passe_correct):
# #     while True:
# #         saisie = input("Entre ton mot de passe : ")
# #         if saisie == mot_de_passe_correct:
# #             print("Accès autorisé ✅")
# #             break
# #         else:
# #             print("Mot de passe incorrect, réessaie...")

# # # Utilisation
# # demander_mot_de_passe("ninja123")




# # def afficher_infos(**kwargs):
# #     print("Kwargs reçus :", kwargs)
# #     for cle, valeur in kwargs.items():
# #         print(f"{cle} → {valeur}")

# # afficher_infos(nom="Ninja", age=21, pays="Côte d’Ivoire"

# éléments = ["mouchoir", "cahier", "stylo"]

# def trouver_élément(liste, objet):
#     if objet in liste:
#         print(f"L'élément '{objet}' est dans la liste ✅")
#     else:
#         print(f"L'élément '{objet}' n'existe pas dans la liste ❌")

# trouver_élément(éléments, "cahier")
# trouver_élément(éléments, "crayon")


class Voiture:
    def __init__(self, marque, modele):
        self.marque = marque   # attribut
        self.modele = modele   # attribut

    def demarrer(self):        # méthode
        print(f"La {self.marque} {self.modele} démarre...")

# Création d'objets
voiture1 = Voiture("Toyota", "Corolla")
voiture2 = Voiture("Tesla", "Model 3")



voiture1.demarrer()
voiture2.demarrer()
