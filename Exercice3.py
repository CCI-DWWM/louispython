while True:
    try:
        n = int(input("Entrez un nombre entier positif : "))
        if n >= 0:
            break
        else:
            print("Veuillez entrer un nombre positif.")
    except ValueError:
        print("Ce n'est pas un nombre entier valide.")

# Calcul de la factorielle
factorielle = 1
for i in range(1, n + 1):
    factorielle *= i

print(f"La factorielle de {n} est {factorielle}.")