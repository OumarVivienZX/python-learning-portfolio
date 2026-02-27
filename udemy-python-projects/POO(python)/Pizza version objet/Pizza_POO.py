class Pizza:

    def __init__(self, nom , prix ,ingredients, vegetarian = False):
        self.nom = nom
        self.prix = prix
        self.ingredients = ingredients
        self.vegetarian = vegetarian

    def Afficher(self):
        if self.vegetarian :
            veg = "- Végétarienne"
        else:
            veg = ""

        print(f"PIZZA : {self.nom} \n PRIX : {self.prix} $ "+veg)
        print(f"INGREDIENTS :{','.join(self.ingredients)}")
        print()

class PizzaPersonnalisee(Pizza):
    PRIX_BASE = 7
    PRIX_ANNEXE = 1.2
    dernier_numero = 0
    def __init__(self):

       PizzaPersonnalisee.dernier_numero +=1
       self.numero = PizzaPersonnalisee.dernier_numero

       super().__init__("personnalisée "+str(self.numero),7,[])
       self.Ajouter_ingredients()
       self.calculer_prix()

    def Ajouter_ingredients(self):
        # Nom de la pizza

        #
        while True:
            ingredient = input(f"Ajouter un ingrédients pour la pizzas personnalisée n°{self.numero} ou Entrer pour arrêter:")

            if ingredient == "":
                return

            self.ingredients.append(ingredient)
            print(f"vous avez ajouté {len(self.ingredients)} ingredient(s). ingrédients ajoutés: {'-'.join(self.ingredients)}")

    def calculer_prix(self):
        self.prix = self.PRIX_BASE + len(self.ingredients) * self.PRIX_ANNEXE



Pizzas = [
 Pizza("Hawaî", 9.6, ("Ananas", "Pastèque", "Mangue", "Oranges"),True),
 Pizza("champignon", 8,("Champignon","Carrote","Abricot","Tomates"),True),
 Pizza("margarita",13.5, ("Crevettes","Oignons verts","Comcombre","Persil"),False),
 Pizza("mexicaine",15,("Saucices","Vourgette","Tomates","Vinaigre de cidre"),False),
 PizzaPersonnalisee(),
 PizzaPersonnalisee()

]


Pizzas.sort(key=lambda e : e.prix)

for pizza in Pizzas:
    pizza.Afficher()
