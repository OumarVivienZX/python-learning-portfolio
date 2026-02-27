import time
import beepy

def choix_utilisateur():
    print("Bienvenu dans le programme de cuissons des oeufs(❁´◡`❁)")
        
    print("""Veuillez choisir une option parmi celles-ci 🍳:
                
        1- Oeuf à la coque :3min
        2- Oeuf mollet :6min 
        3- Oeuf dur :9min""")
    
    choix_str = input("Votre choix : ")

    try:
        choix_int = int(choix_str)
    except ValueError:
        print("❌ ERREUR : Vous devez entrer un chiffre pour le choix ❌")
        return choix_utilisateur()  # Relance la fonction pour un nouveau choix

    # Vérifie les options disponibles
    if choix_int == 1:
        d = 10 # 3 minutes
    elif choix_int == 2:
        d = 6*60  # 6 minutes
    elif choix_int == 3:
        d = 9*60  # 9 minutes
    else:
        print("❌ ERREUR : Le choix ne fait pas partie des options disponibles ❌")
        return choix_utilisateur()  # Relance la fonction pour un nouveau choix

    return d

# Obtenir la durée de cuisson en fonction du choix de l'utilisateur
durée = choix_utilisateur()

print("Cuisson en cours 🍳...")

# Boucle de décompte de la durée de cuisson
while durée > 0:
    min = durée // 60  # Calcul des minutes restantes
    sec = durée % 60   # Calcul des secondes restantes
    
    print(f"Temps restant :{min:02d}:{sec:02d}", end="", flush=True)
    
    # Affiche les points pendant 10 secondes
    for i in range(10):
        time.sleep(1)
        print(".", end="", flush=True)
    print()  # Nouvelle ligne après les points
     
    durée -= 10  # Réduit la durée de 10 secondes

print("FIN DE LA CUISSON 🍳😋")
beepy.beep(sound=2)
