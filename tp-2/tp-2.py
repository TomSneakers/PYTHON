import os
import csv
import json
import pathlib
import statistics

# Dictionnaire des élèves
dicEleves = {
    'titi': {'notes': {'tp1': 10, 'tp2': 13, 'tp3': 17}, 'appréciation': 'moyenne'},
    'toto': {'notes': {'tp1': 19, 'tp2': 11, 'tp3': 14}, 'appréciation': 'Très Bien'},
    'tata': {'notes': {'tp1': 15, 'tp2': 8, 'tp3': 13}, 'appréciation': 'Bonne'},
    'tutu': {'notes': {'tp3': 15, 'tp4': 13}, 'appréciation': 'Bonne'},
}

# Création du dossier 'eleves'
eleves_path = pathlib.Path('tp-2/eleves')
eleves_path.mkdir(parents=True, exist_ok=True)

# Création des dossiers par élève
for eleve, info in dicEleves.items():
    eleve_path = eleves_path / eleve
    eleve_path.mkdir(parents=True, exist_ok=True)

    # Création du fichier appréciation.txt pour chaque élève
    with open(eleve_path / 'appreciation.txt', 'w') as f:
        f.write(info['appréciation'])

    # Création du fichier notes.csv pour chaque élève
    with open(eleve_path / 'notes.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['TP', 'Note'])
        for tp, note in info['notes'].items():
            writer.writerow([tp, note])

# Création du fichier json dans le dossier 'eleves'
data = {}
for eleve, info in dicEleves.items():
    notes = list(info['notes'].values())
    data[eleve] = {'moyenne': statistics.mean(notes), 'min': min(notes), 'max': max(notes)}

with open(eleves_path / 'eleves.json', 'w') as f:
    json.dump(data, f, indent=4)