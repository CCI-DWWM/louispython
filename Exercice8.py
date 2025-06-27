def afficher_nom_encadre():
    nom = input("Quel est votre prénom ? ")
    longueur = len(nom)
    ligne_haut = "┌" + "─" * (longueur + 2) + "┐"
    ligne_milieu = f"│ {nom} │"
    ligne_bas = "└" + "─" * (longueur + 2) + "┘"

    print(ligne_haut)
    print(ligne_milieu)
    print(ligne_bas)


# Appel de la fonction
afficher_nom_encadre()