# Programa che converte unità astronomica in metri
# introduce isinstance per verificare il tipo di dato e raise per sollevare un eccezione se il dato non è valido
# pytest è un framework di test per Python che semplifica la scrittura e l'esecuzione di test automatizzati.
# 

def main():
    while True:
        au = input("AU: ")
        try:
            au = float(au)
            break
        except ValueError:
            continue

    print(f"{au} AU is {convert(au)} m")

def convert(au):
    if not isinstance(au, (int, float)):
        raise TypeError("AU must be a number")
    return au * 149597870700

if __name__ == "__main__":
    main()

# Per eseguire i test, è necessario installare pytest e poi eseguire il comando "pytest" nella directory del progetto. Pytest cercherà automaticamente i file di test e li eseguirà, mostrando i risultati dei test.
# in un altro file di test , importo la funzione da testare e scrivo i test usando assert per verificare che i risultati siano corretti. Se tutti i test passano, non ci sarà output, altrimenti verranno mostrati i dettagli degli errori.
# esempio:

import pytest

from pytest-21.py import convert

def test_conversion():
    assert convert(1) == 149597870700    # nel terminale : pytest nomefile.py per vedere se tutto funziona correttamente
    assert convert(0) == 0               # se tutto è corretto non da output , se c'è un errore da dettagli dell'errore
    assert convert(2) == 299195741400    # altri test per verificare la correttezza della funzione

def test_invalid_input():
    with pytest.raises(TypeError):
        convert("not a number")           # test per verificare che la funzione sollevi un'eccezione quando l'input non è valido

def test_float_conversion():
    assert convert(0.001) == pytest.approx(149597870.7, abs = 1e-10)  # test per verificare che la funzione funzioni correttamente anche con numeri decimali
# aggiungendo una tolleranza

