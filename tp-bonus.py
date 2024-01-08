import random
# Initialisation des scores
score_joueur1 = 0
score_joueur2 = 0

while True:
    # Chaque joueur tire une fois
    tirage1 = random.randint(1, 6)
    tirage2 = random.randint(1, 6)

    # On ajoute un point au joueur avec la valeur la plus forte
    if tirage1 > tirage2:
        score_joueur1 += 1
    elif tirage2 > tirage1:
        score_joueur2 += 1

    # Chaque joueur tire 5 fois
    tirages1 = [random.randint(1, 6) for _ in range(5)]
    tirages2 = [random.randint(1, 6) for _ in range(5)]

    # On totalise les deux plus fortes valeurs et la plus faible
    total1 = sum(sorted(tirages1)[-2:]) + min(tirages1)
    total2 = sum(sorted(tirages2)[-2:]) + min(tirages2)

    # On ajoute un point au joueur avec la valeur la plus forte
    if total1 > total2:
        score_joueur1 += 1
    elif total2 > total1:
        score_joueur2 += 1

    # On affiche les résultats
    print("Score du joueur 1 : ", score_joueur1)
    print("Score du joueur 2 : ", score_joueur2)

    # On demande à l'utilisateur s'il veut continuer ou arrêter
    reponse = input("Entrez 'rs' pour recommencer ou 'stop' pour arrêter : ")
    if reponse == 'stop':
        break