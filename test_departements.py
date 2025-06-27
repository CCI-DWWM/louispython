# test_departements.py
import Exercice9

def test_get_nom_departement_valid():
    assert get_nom_departement("75") == "Paris"
    assert get_nom_departement("41") == "Loir-et-Cher"

def test_get_nom_departement_invalide():
    assert get_nom_departement("999") == "Département inconnu"