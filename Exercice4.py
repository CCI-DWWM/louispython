def compter_voyelles_consonnes(phrase):
    voyelles = "aeiouyAEIOUY"
    consonnes = "bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ"

    nb_voyelles = 0
    nb_consonnes = 0

    for caractere in phrase:
        if caractere in voyelles:
            nb_voyelles += 1
        elif caractere in consonnes:
            nb_consonnes += 1

    return nb_voyelles, nb_consonnes

phrase = input("Entrez une phrase : ")

voyelles, consonnes = compter_voyelles_consonnes(phrase)

print(f"Nombre de voyelles : {voyelles}")
print(f"Nombre de consonnes : {consonnes}")
