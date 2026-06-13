# La Standard Library 
# é una raccolta di moduli e pacchetti predefiniti che forniscono funzionalità aggiuntive per facilitare lo sviluppo di applicazioni.

# import 
# modules

import random

coin = random.choice(["heads","tails"])
print(coin)

# Alternativa di import con from/ 

from random import choice

coin = choice(["heads","tails"])
print(coin)

# Randint -> random integer (a,b) [da 0 a 10]

import random

number = random.randint(1,10)
print(number)

# Random.shuffle(x) / mescola la lista che viene data

import random

cards = ["jack","queen","king"]
random.shuffle(cards)
for card in cards :
    print(card)

# Statistic Library
# modulo di statistica utile per mediana,average,moda ecc..

import statistics

print(statistics.mean([100,90]))

# Command-line arguments
# sys / sistema di comando
# sys.argv -> argument vector -> riceverà dall'utente una (lista) dipendente dal numero inserito nelle prentesi quadre
# sys.argv FORNISCE TUTTE LE PAROLE DIGITATE AL PROMPT,incluso il nome del programma
import sys

print("hello, my name is",sys.argv[0])
# sys,argv conserva 1 argomento,se scrivo 0 comprare i nome del sistema(argomento 0)
# IndexError = errore piu comune di python,con liste ecc...

# Gestire l'Errore IndexError

import sys

try:
    print("hello, my name is", sys.argv[1])
except IndexError:
    print("Too few arguments")

# import sys con condizioni p.s. genererà un errore SyntaxError

import sys

if len(sys.argv) < 2:
    print("too few arguments")
elif len(sys.argv) > 2:
    print("too many arguments")
else:
    print("hello, my name is", sys.argv[1])

# Error Handling separation

import sys
# Check for errors
if len(sys.argv) < 2:
    print("too few arguments")
elif len(sys.argv) > 2:
    print("too many arguments")

# print name tags
print("hello, my name is", sys.argv[0])

# Correggendo e introducendo sys.exit a codice qui sopra
# sys.exit = può accettare diversi tipi di input,ma se passo una string "come questa", stamperà quella stringa per me. TIPO RETURN/EXCEPT
# e uscirà dal programma in quel momento. tipo un mix di return/except/break
import sys
# Check for errors
if len(sys.argv) < 2:
    sys.exit("too few arguments")
elif len(sys.argv) > 2:
    sys.exit("too many arguments")

# print name tags
print("hello, my name is", sys.argv[1])

#---------------------------------------------------------------------------------------
# multipli input name tags/ for looping /LOOP/ LOOPING

import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv:
    print("hello, my name is", arg) # Output 0,sistema; 1, primo nome e cosi via..

# slices [ numero/oppure vuoto : numero/oppure vuoto]

import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:]:
    print("hello, my name is", arg)

# Packages / libreria di terze parti / PyPI.org
# cowsay pack 
# pip = packages manager 
# ARTE ASCII
# Esempio : 
# (terminal) pip install cowsay
# import cowsay
# import sys
#
# if len(sys.argv) == 2:
#     cowsay.cow("hello, " + sys.argv[1])
#
# output :
#        \   ^__^
#         \  (oo)\_______
#            (__)\       )\/\
#                ||----w |
#                ||     ||
#-------------------------------------------------------------------------------

# # Esempio : 
# (terminal) pip install cowsay
# import cowsay
# import sys
#
# if len(sys.argv) == 2:
#     cowsay.trex("hello, " + sys.argv[1])

# output :
# dinosauro

#-------------------------------------------------------------------------------

# API's application program integrations
# requests libray 

# import requests

# JSON JavScript Object Notation
# scambio di dati tra computer

# import requests
# import sys
#
# if len(sys.argv) != 2
#    sys.exit()
#
# response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
# print(response.json())
#
# -----------JSON LIBRARY PER CAPIRCI MEGLIO-----------------
#
# import json
# import requests
# import sys
#
# if len(sys.argv) != 2
#    sys.exit()
#
# response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
# print(json.dumps(response.json(), indent=2 ))
#
#----indent==2 -> tutta la lista viene indentata
#
# --- COME MANIPOLARE IL FILE DI RISULTATO -- PER CERCARE QUALCOSA DI SPECIFICO--------------------
#
# import json
# import requests
# import sys
#
# if len(sys.argv) != 2
#    sys.exit()
#
# response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
#
# o = responde.json()          -> creo una variabile che contiene l'oggetto JSON che mi interessa
# for result in o["results"]:   -> per ogni result in oggetto ["chiave"], stmpa 
#     print(result["trackName"])
#
#----------------------------------------------------------------------------------------------------
#def main():
#     hello("world")
#    goodbye("world")

#def hello (name):
#    print(f'hello, {name}')

#def goodabye(name):
#     print(f'goodbye,{name}')

#if __name__ == "__main__":
#    main()

# Esempio con import sys e un altro file sayings.py

#import sys
#from sayings import hello

#if len(sys.argv) ==2:
#    hello(sys.argv[1])

# __name__ -> è una variabile speciale in Python che rappresenta il nome del modulo corrente.
#
# Quando un modulo viene eseguito direttamente, __name__ viene impostato su "__main__".


# Riassunto:
# - La Standard Library è una raccolta di moduli e pacchetti predefiniti che forniscono funzionalità aggiuntive per facilitare lo sviluppo di applicazioni.
# - Per importare un modulo, basta usare la parola chiave import seguita dal nome del modulo.
# - Per importare una funzione specifica da un modulo, basta usare la parola chiave from seguita dal nome del modulo, la parola chiave import e il nome della funzione.
# - Per gestire gli errori, basta usare il costrutto try/except e gestire le eccezioni specifiche che si vogliono gestire.
# - Per fare una richiesta API, basta usare la funzione requests.get() e passare l'URL del sito a cui si vuole fare la richiesta.
# - Per controllare se la richiesta è andata a buon fine, basta usare il metodo raise_for_status() e gestire l'eccezione HTTPError se la richiesta non è andata a buon fine.
# - Per ottenere i dati dalla risposta, basta usare il metodo json() e accedere ai dati usando le chiavi del JSON. 
