# Unit Test

def main():
    x = int(input("What's x? "))
    print("x squared is" , square(x))

def square(n):
    return n * n

if __name__== "__main__":
    main()

# file da testare su un altro file.
# crei un atro file e usi from e import (vedere l1altro file)

# Assert nuova parola :
# se un acondizione è falsa dirà errore

# assert e raise:

# assert si usa per verifiche interne e debugging
# puo essere disattivato con -o 
# genera solo AssertionError 
# sintassi: assert condizione, "messaggio di errore"


# raise si usa per errori reali e gestione logica 
# è sempre attivo 
# puo sollevare una qualsiasi eccezioni 
# sintassi: raise ValueError("messaggio Valore non valido in questo caso")


# raise solleva un eccezione
# assert verifica una condizione 


def main():
    name = input("Whats your name? ")
    print(hello(name))

def hello(to="world"):
    return f"hello, {to}"

if __name__ == "__main__":
    main()

# Adesso dovresti creare un altro file per testare la funzione hello, importarla e scrivere dei test per verificare che funzioni correttamente con diversi input, incluso il caso predefinito.

# esempio di test per la funzione hello:

#from hello import hello

def test_default():
    assert hello() == "Hello, world"
    
def test_arguement():
    for name in ["Alice", "Bob", "Charlie"]:
        assert hello(name) == f"Hello, {name}"  

# pytest file.py per il test della funzione hello

# mkdir test
# code test/test_hello.py ( file di esempio)
# code test/__init__.py ( file vuoto per indicare che è una cartella di test)

# cosi si crea un PACKAGE di test e pytest lo riconosce automaticamente

# poi pytest test ; per eseguire tutti i test nella cartella test