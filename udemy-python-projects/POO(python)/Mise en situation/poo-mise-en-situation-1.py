# POO EXERCICE DE MISE EN SITUATION 1
# genre
#   False : Femme
#   True  : Homme
class Personne:
    def __init__(self,genre: bool, nom: str = "",age: int = 0 ):
        self.nom = nom   # crée une variable d'instance : nom
        self.age = age
        self.genre = genre
        print("Constructeur personne " + self.nom)
        if self.nom == "":
            self.nom = self.demander_nom()

    def SePresenter(self):
        # Bonjour, je m'appelle Jean, j'ai 30 ans
        # Je suis majeur
        self.présentation()
        genre_str = "Masculin" if self.genre else"Feminin"
        print(f"Genre : {genre_str}")

        e_optionnel = "" if self.genre else "e"

        if self.EstMajeur():
            print("Je suis majeur" + e_optionnel)
        else:
            print("Je suis mineur" + e_optionnel)
        print()

    def EstMajeur(self):
        return self.age >= 18

    def demander_nom(self) :
            self.nom = input("veuillez entrer votre nom :")
            return self.nom
    def présentation(self):
         if self.age == 0 :           
            return print("Bonjour, je m'appelle " + self.nom )
         else:           
             return  print("Bonjour, je m'appelle " + self.nom  + " j'ai " + str(self.age) + " ans")
    

personne1 = Personne(True,"jean")
personne1.SePresenter()

personne2 = Personne( False,"Emilie", 17)
personne2.SePresenter()