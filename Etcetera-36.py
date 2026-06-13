# controllare programmi dalla linea di comando, terminale?

import sys

if len(sys.argv) == 1:
    print("meow")
else:
    print("usage: meows.py")      # Output "meow", se non si inserisce altre cose dopo il file che stiamo usando

# swithces and flags / far capire al programma che -n 3 è un comando che indica di ripeter 3 volte ((Esempio))

import sys

if len(sys.argv) == 1:
    print("meow")
elif len(sys.argv) == 3 and sys.argv[1] == "-n":
    n = int(sys.argv[2])
    for _ in range(n):
        print("meows")
else:
    print("usage: meows.py")

# Trduzione =  Controllo se l'utente mi ha dato 3 argomenti: 
# il nome del file/programma, -n e un numero.
# Se è così, converto il numero in un intero e lo uso per ripetere "meow" quel numero di volte.
# Altrimenti, stampo un messaggio di utilizzo.

# Complicando il codice:  argparse
# argparse è una libreria che semplifica la gestione degli argomenti della riga di comando, rendendo il codice più leggibile e robusto.

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-n")
args = parser.parse_args()

for _ in range(int(args.n)):
    print("meow")

## argparse è più potente e flessibile di sys.argv, e permette di gestire facilmente argomenti opzionali, posizionali, e di fornire messaggi di aiuto automatici.

# Migliorando e spiegando il codice con argparse:

import argparse

parser = argparse.ArgumentParser(description="Meow like a cat")
parser.add_argument("-n", default= 1,  help="Number of times to meow", type=int)
args = parser.parse_args()

for _ in range(int(args.n)):
    print("meow")



# ------------------- Unpacking ----------------------------------------
# unpacking è una tecnica che permette di assegnare i valori di una lista o di una tupla a più variabili in una sola riga di codice.

def total(galleons, sickles, knuts):
    return (galleons * 17 * 29 + sickles) * 29 + knuts

print(total(100, 50, 25), "knuts")


# mettendo i valori in una lista, posso fare così:
def total(galleons, sickles, knuts):
    return (galleons * 17 * 29 + sickles) * 29 + knuts

coins = [100, 50, 25]

print(total(coins[0],coins[1],coins[2]), "knuts")

# Ma con unpacking, posso fare così:
def total(galleons, sickles, knuts):
    return (galleons * 17 * 29 + sickles) * 29 + knuts

coins = [100, 50, 25]

print(total(*coins), "knuts")
# * prima di coins indica che voglio unpackare la lista, cioè prendere i suoi elementi e passarli come argomenti separati alla funzione total. In questo modo, coins[0] diventa galleons, coins[1] diventa sickles, e coins[2] diventa knuts.

# Se invece di una lista, ho un dizionario con le chiavi che corrispondono ai nomi degli argomenti della funzione, posso fare così:

def total(galleons, sickles, knuts):
    return (galleons * 17 * 29 + sickles) * 29 + knuts

coins = {"galleons": 100, "sickles": 50, "knuts": 25}

print(total(**coins), "knuts")

# invece di : print(total)(coins["galleons"], coins["sickles"], coins["knuts"]), "knuts")
# ** prima di coins indica che voglio unpackare il dizionario, cioè prendere le sue coppie chiave-valore e passarle come argomenti di parola chiave alla funzione total.



# ----------------- *args e **kwargs ----------------------------------------
# *args e **kwargs sono convenzioni che indicano rispettivamente una lista di argomenti posizionali e un dizionario di argomenti di parola chiave.

def f(*args, **kwargs):
    print("Positional:", args)

f(100, 50, 25)
# Output: Positional: (100, 50, 25) // posso passare tutti gli argomenti che voglio, e saranno raccolti in una tupla chiamata args.

def f(*args, **kwargs):
    print("Named:", kwargs)

f(galleons=100, sickles=50, knuts=25)
# Output: Named: {'galleons': 100, 'sickles': 50, 'knuts': 25} // posso passare tutti gli argomenti che voglio, e saranno raccolti in un dizionario chiamato kwargs.
# *args e **kwargs sono utili quando non si sa in anticipo quanti argomenti si vogliono passare a una funzione, o quando si vuole permettere agli utenti di passare argomenti opzionali senza doverli specificare tutti nella definizione della funzione.



# ------------------- map ----------------------------------------
# map è una funzione built-in che applica una funzione a ogni elemento di un iterabile (come una lista) e restituisce un nuovo iterabile con i risultati.

def main():
    yell("This is CS50")


def yell(phrase):
    print(phrase.upper())


if __name__ == "__main__":
    main()
# Output: THIS IS CS50


# usando lista :

def main():
    yell("This is CS50")

def yell(words):
    uppercased = []
    for word in words:
        uppercased.append(word.upper())
    print(*uppercased)

if __name__ == "__main__":
    main()

# Output: THIS IS CS50


# usando *args:

def main():
    yell("This is CS50")

def yell(*words):   # *words indica che voglio accettare un numero variabile di argomenti posizionali, e che questi saranno raccolti in una tupla chiamata words.
    uppercased = []
    for word in words:
        uppercased.append(word.upper())
    print(*uppercased)

if __name__ == "__main__":
    main()
    
# Output: THIS IS CS50


# Usando Map(): // map(functions, iterable) // la funzione map prende due argomenti: una funzione e un iterabile. Applica la funzione a ogni elemento dell'iterabile e restituisce un nuovo iterabile con i risultati.

def main():
    yell("This is CS50")

def yell(*words):
    uppercased = map(str.upper, words)  # str.upper è una funzione built-in che prende una stringa e restituisce la stessa stringa in maiuscolo. map applica questa funzione a ogni elemento di words, restituendo un iterabile di parole maiuscole.
    print(*uppercased)

if __name__ == "__main__":
    main()
    
# Output: THIS IS CS50

# map è più conciso e leggibile rispetto a un ciclo for, e può essere più efficiente in alcuni casi. Tuttavia, è importante ricordare che map restituisce un iterabile, quindi se si vuole ottenere una lista o una tupla, è necessario convertirlo esplicitamente usando list() o tuple().



# ------------------- List Comprehensions ----------------------------------------
# List comprehensions sono una sintassi concisa per creare liste a partire da iterabili esistenti, applicando una trasformazione o un filtro a ogni elemento.

def main():
    yell("This is CS50")

def yell(*words):
    uppercased = [word.upper() for word in words]  # Questa è una list comprehension che crea una nuova lista uppercased. Per ogni word in words, applica il metodo upper() e aggiunge il risultato alla lista uppercased.
    print(*uppercased)

if __name__ == "__main__":
    main()

# Output: THIS IS CS50



# 