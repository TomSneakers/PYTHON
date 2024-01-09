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

def create_files(dicEleves):
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

def add_student(dicEleves):
    name = input("Nom de l'élève: ")
    dicEleves[name] = {'notes': {}, 'appréciation': ''}

def add_note(dicEleves):
    name = input("Nom de l'élève: ")
    tp = input("Nom du TP: ")
    note = int(input("Note: "))
    dicEleves[name]['notes'][tp] = note

def modify_appreciation(dicEleves):
    name = input("Nom de l'élève: ")
    appreciation = input("Nouvelle appréciation: ")
    dicEleves[name]['appréciation'] = appreciation

def list_students(dicEleves):
    for name, info in dicEleves.items():
        print(f"Nom: {name}, Notes: {info['notes']}, Appréciation: {info['appréciation']}")

def main():
    create_files(dicEleves)
    while True:
        command = input("Voici toute les commandes: \n add \n notes \n appr \n list \n quitter \n Commande: ")
        if command == "add":
            add_student(dicEleves)
        elif command == "notes":
            add_note(dicEleves)
        elif command == "appr":
            modify_appreciation(dicEleves)
        elif command == "list":
            list_students(dicEleves)
        elif command == "quitter":
            break
        else:
            print("Pas compris")

    create_files(dicEleves)

if __name__ == "__main__":
    main()