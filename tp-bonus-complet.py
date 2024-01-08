import random

# Initialiser les scores
score_joueur1 = 0
score_joueur2 = 0

score_total_joueur1 = 0
score_total_joueur2 = 0

# Simuler 10000 manches
for _ in range(10000):
    # Chaque joueur tire une fois
    tirage1 = random.randint(1, 6)
    tirage2 = random.randint(1, 6)
    
    # Ajouter un point au joueur avec le nombre le plus élevé
    if tirage1 > tirage2:
        score_joueur1 += 1
    elif tirage2 > tirage1:
        score_joueur2 += 1
    
    
    # Chaque joueur tire 5 fois
    tirages1 = [random.randint(1, 6) for _ in range(5)]
    tirages2 = [random.randint(1, 6) for _ in range(5)]
    
    # Totaliser les deux plus fortes valeurs et la plus faible
    total1 = sum(sorted(tirages1)[-2:]) + min(tirages1)
    total2 = sum(sorted(tirages2)[-2:]) + min(tirages2)
    
    # Ajouter un point au joueur avec le nombre le plus élevé
    score_total_joueur1 = score_joueur1
    score_total_joueur2 = score_joueur2
    if total1 > total2:
        score_total_joueur1 += 1
    elif total2 > total1:
        score_total_joueur2 += 1

# Afficher les scores
print(f"Score du joueur 1: {score_joueur1}")
print(f"Score du joueur 2: {score_joueur2}")

print(f"Score total du joueur 1: {score_total_joueur1}")
print(f"Score total du joueur 2: {score_total_joueur2}")

# Déterminer le gagnant
if score_joueur1 > score_joueur2:
    print("Le joueur 1 a gagné!")
elif score_joueur2 > score_joueur1:
    print("Le joueur 2 a gagné!")
else:
    print("C'est un match nul!")

# Déterminer le nombre de manches null totale sur les 10000 manches
manches_nulles = 10000 - score_joueur1 - score_joueur2
print(f"Nombre de manches nulles: {manches_nulles}")
