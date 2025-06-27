import Exercice7.py

def test_Exercice7():
    assert Exercice7.est_premier(5)
    assert not Exercice7.est_premier(6)
    assert Exercice7.est_premier(7)
    assert not Exercice7.est_premier(8)
    assert not Exercice7.est_premier(9)
    assert not Exercice7.est_premier(33333333333333)
    assert not Exercice7.est_premier(10000000000)
    assert Exercice7.est_premier(9576890767)