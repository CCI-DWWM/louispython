from datetime import datetime

prenom = input("Entrez votre prénom : ")
nom = input("Entrez votre nom : ")

while True:
    annee_naissance = input("Entrez votre année de naissance : ")
    if annee_naissance.isdigit():
        annee_naissance = int(annee_naissance)
        break
    else:
        print("Veuillez entrer une année valide (chiffres uniquement).")

annee_actuelle = datetime.now().year
age = annee_actuelle - annee_naissance

print(f"Bonjour {prenom} {nom}, vous avez {age} ans.")