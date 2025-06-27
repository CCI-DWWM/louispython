from colorama import init, Fore

def afficher_nom_encadre():
    init(autoreset=True)  # Initialise colorama
    nom = input("Quel est votre prénom ? ")
    longueur = len(nom)
    ligne_haut = "┌" + "─" * (longueur + 2) + "┐"
    ligne_milieu = f"│ {Fore.RED}{nom}{Fore.RESET} │"
    ligne_bas = "└" + "─" * (longueur + 2) + "┘"

    print(ligne_haut)
    print(ligne_milieu)
    print(ligne_bas)

afficher_nom_encadre()