import datetime
date = datetime.datetime.now()
# récupération de l'année en cour
annee_en_cours = date.year

anneeSaisie = input("annee de naissance : ")
# calcul de l'age l'année saisie est une chaine de caractere, il faut la convertir en entier
age = annee_en_cours - int(anneeSaisie) 
print ('age : ' + str(age))

# calcul du mois
ageEnMois = age * 12
print ('age En Mois : ' + str(ageEnMois))

# calcul en jour
anneeBisextile = int(age / 4)
ageEnJours = age * 365 + anneeBisextile
print ('age En Jours : {}'.format(ageEnJours))

# calcul en semaine
ageEnSemaine = age * 52
ageEnSemaine = int(ageEnJours / 7)
print ('age En Semaine :', ageEnSemaine)

#Comptage de lettres et de mots d’une chaine de caractère saisie​

chaine = input("saisir une chaine de caractere : ")

#Compter le nombre de voyelle d’une chaine de caractère saisie​

voyelle = 0
for i in chaine:
    if i in "aeiouyAEIOUY":
        voyelle += 1
print("nombre de voyelle : ", voyelle)

#Compter le nombre de consonne d’une chaine de caractère saisie​

consonne = 0
for i in chaine:
    if i in "bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ":
        consonne += 1
print("nombre de consonne : ", consonne)

#Compter le nombre de mot d’une chaine de caractère saisie​

mot = 1
for i in chaine:
    if i in " ":
        mot += 1
print("nombre de mot : ", mot)

#Renvoyer une liste de mot à partir d’une phrase​

phrase = input("saisir une phrase : ")
phrase = phrase.split()
print("liste de mot : ", phrase)

#Vérifier la présence d’une lettre dans d’une chaine de caractère saisie​
chaine = input("saisir une chaine de caractere : ")
lettre = input("saisir une lettre : ")
if lettre in chaine:
    print("la lettre est presente")
else:
    print("la lettre n'est pas presente")

#Vérifier la présence d’un mot dans une liste (retourne sa position dans le tableau)​
phrase = input("saisir une phrase : ")
phrase = phrase.split()
mot = input("saisir un mot : ")
if mot in phrase:
    print("le mot est present")
else:
    print("le mot n'est pas present")

#ajoute un mot si il n’est pas présent dans un tableau​
phrase = input("saisir une phrase : ")
phrase = phrase.split()
mot = input("saisir un mot : ")
if mot in phrase:
    print("le mot est present")
else:
    print("le mot n'est pas present")
    print("Ancienne liste de mot : ", phrase)

    phrase.append(mot)
    print("le mot vient d'etre ajouter à la liste")
    print("Nouvelle liste de mot : ", phrase)

#Supprimer un mot d’une liste​
phrase = input("saisir une phrase : ")
phrase = phrase.split()
mot = input("saisir un mot : ")
if mot in phrase:
    print("le mot est present")
    print("Ancienne liste de mot : ", phrase)

    phrase.remove(mot)
    print("le mot vient d'etre supprimer de la liste")
    print("Nouvelle liste de mot : ", phrase)
else:
    print("le mot n'est pas present")
#renvoi le tableau lorsque l'on ecrit tableau
mot = input("saisir tableau pour retrouner phrase : ")

if mot == "tableau":
    print("le tableau est : ", phrase)



