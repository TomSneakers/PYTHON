import datetime

# Initialiser un dictionnaire pour stocker le nombre de vendredi 13 par année
vendredi_13_par_annee = {}

# Parcourir chaque année de 1900 à l'année actuelle
for annee in range(1900, datetime.datetime.now().year + 1):
    # Parcourir chaque mois de chaque année
    for mois in range(1, 13):
        # Si le 13ème jour du mois est un vendredi (5 en Python)
        if datetime.datetime(annee, mois, 13).weekday() == 4:
            # Si l'année est déjà dans le dictionnaire, incrémenter le compteur
            if annee in vendredi_13_par_annee:
                vendredi_13_par_annee[annee] += 1
            # Sinon, ajouter l'année au dictionnaire avec un compteur de 1
            else:
                vendredi_13_par_annee[annee] = 1

# Parcourir le dictionnaire et imprimer chaque année et son nombre de vendredi 13
for annee, nombre in vendredi_13_par_annee.items():
    print(f"Année: {annee}, Nombre de vendredi 13: {nombre}")

# Déterminer la première et la dernière année avec la plus de V13​
# On récupère la première année avec le plus de vendredi 13
premiere_annee = min(vendredi_13_par_annee, key=vendredi_13_par_annee.get)
# On récupère le nombre de vendredi 13 de cette année
nombre_premiere_annee = vendredi_13_par_annee[premiere_annee]
# On récupère la dernière année avec le plus de vendredi 13
derniere_annee = max(vendredi_13_par_annee, key=vendredi_13_par_annee.get)
# On récupère le nombre de vendredi 13 de cette année
nombre_derniere_annee = vendredi_13_par_annee[derniere_annee]

# On affiche les résultats
print(f"Première année avec le plus de vendredi 13: {premiere_annee}, Nombre de vendredi 13: {nombre_premiere_annee}")
print(f"Dernière année avec le plus de vendredi 13: {derniere_annee}, Nombre de vendredi 13: {nombre_derniere_annee}")

# Répartir de 0 à 4 le nombre d’année ​
# avec 0 vendredi 13, 1 vendredi 13, 2 vendredi 13, 3 vendredi 13 et 4 vendredi 13
# On initialise un dictionnaire avec 0 vendredi 13, 1 vendredi 13, 2 vendredi 13, 3 vendredi 13 et 4 vendredi 13
nombre_vendredi_13 = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0}
# On parcourt le dictionnaire des vendredi 13 par année
for nombre in vendredi_13_par_annee.values():
    # On incrémente le compteur correspondant au nombre de vendredi 13
    # seulement si le nombre de vendredi 13 est entre 0 et 4
    if nombre in nombre_vendredi_13:
        nombre_vendredi_13[nombre] += 1

# On affiche les résultats
print(f"Nombre d'années avec 0 vendredi 13: {nombre_vendredi_13[0]}")
print(f"Nombre d'années avec 1 vendredi 13: {nombre_vendredi_13[1]}")
print(f"Nombre d'années avec 2 vendredi 13: {nombre_vendredi_13[2]}")
print(f"Nombre d'années avec 3 vendredi 13: {nombre_vendredi_13[3]}")
print(f"Nombre d'années avec 4 vendredi 13: {nombre_vendredi_13[4]}")
