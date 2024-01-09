import os
import csv
import json
import pathlib

#Toute les donnée seront gerer en brut dans le code
# Liste des élèves
eleves = ['tata', 'titi', 'toto']

# Création du dossier 'eleves'
eleves_path = pathlib.Path('tp-2/eleves')
eleves_path.mkdir(parents=True, exist_ok=True)

# Création des dossiers par élève
for eleve in eleves:
    if not os.path.exists(f'eleves/{eleve}'):
        os.makedirs(f'eleves/{eleve}')

    # Création du fichier appréciation.txt pour chaque élève
    with open(f'eleves/{eleve}/appreciation.txt', 'w') as f:
        f.write(f"Appréciation pour {eleve}")

    # Création du fichier notes.csv pour chaque élève
    with open(f'eleves/{eleve}/notes.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Matière', 'Note'])
        writer.writerow(['Maths', 15])
        writer.writerow(['Français', 14])

# Création du fichier json dans le dossier 'eleves'
data = {}
for eleve in eleves:
    data[eleve] = {'moyenne': 14.5, 'min': 10, 'max': 18}

with open('eleves/eleves.json', 'w') as f:
    json.dump(data, f, indent=4)