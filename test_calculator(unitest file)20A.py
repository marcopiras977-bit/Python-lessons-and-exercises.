import py_compile
from unittest import square

def main():
    test_square()

def test_square():

    if square(2) != 4:
        print("2 square was not 4")
    if square(3) != 9:
        print("3 squared was not 9")

if __name__ == "__main__":
    main()

# Questo serve per fare dei test specifici da un altro file. 
# from nome file import che cosa
# esempio di test della funzione square
# SE , l' Output del altro file è Corretto, questo file non dara Output

# Assert: Asserzione / test di verifica
# serve er controllare se una condizione sia vera
# Sintassi : assert condizione , "messaggio di errore"
# NON usare per verificare gli errori dell' utente , controlli di sicurezza, validazioni di produzione
# Si usa per debugging e test , non per gestione errori

from unittest import square

def main():
    test_square()

def test_square():

    assert square(2) == 4
    assert square(3) == 9 

if __name__ == "__main__":
    main()

# AssertionError # Gestione Asserzione dell' Errore #---------------------

from unittest import square

def main():
    test_square()

def test_square():
    try:
        assert square(2) == 4
    except AssertionError:
        print("2 square was not 4")

    try:
        assert square(3) == 9
    except AssertionError:
        print("3 square was not 9")
    
if __name__ == "__main__":
    main()

# 
# pytest - docs.pytest.org ------------------------------------------
# mi informa e testa il file per me

from unittest import square

def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(0) == 0

# ne terminale : pytest nomefile.py
# se tutto è corretto non da output , se c'è un errore da dettagli dell'errore
# pytest -v nomefile.py da dettagli anche se tutto è corretto

# Separare il test in più funzioni per testare casi specifici e ricevere errori piu specifici:

from unittest import square

def test_positive():
    assert square(2) == 4
    assert square(3) == 9

def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9

def test_zero():
    assert square(0) == 0


#à#à#à#à#à#à#à#à#à#à#à#à#à#à#à#à#à#à#
# inserendo un errore di str invece che int

import pytest

from unittest import square

def test_positive():
    assert square(2) == 4
    assert square(3) == 9

def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9

def test_zero():
    assert square(0) == 0

def test_str():
    with pytest.raises(TypeError):
        square("cat")

# pytest.raises() serve per verificare che un certo tipo di eccezione venga sollevata quando si esegue un codice specifico. In questo caso, stiamo verificando che la funzione square sollevi un TypeError quando viene passata una stringa invece di un numero. Se la funzione solleva effettivamente un TypeError, il test passerà. Se non solleva alcuna eccezione o solleva un'eccezione diversa, il test fallirà.  
# 