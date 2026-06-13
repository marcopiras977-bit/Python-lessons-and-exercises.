# Regular Expressions / regex/es

# Sarebbe un modello per confrontare un certo tipo di dati,spesso input dell'utente

# Validazione di un email

# file: validate.py

email = input("Whats ur email? ").strip()

if "@" in email and "." in email:
    print("valid")
else: 
    print("invalid")


# per farlo piu concreto e efficacie
username, domain = email.split("@") 

if username and "." in domain:
    print("Valid")
else:
    print("Invalid")


# piu preciso per specificare il dominio
email = input("Whats ur email? ").strip()
username, domain = email.split("@") 
if username and "." in domain.endswith(".edu"):
    print("Valid")
else:
    print("Invalid")


# Migliorare tutto questo con una libreria Python
# REGULAR ESPRESSION 
# re - re.search(pattern, string, flags=0)
import re

email = input("Whats ur email? ").strip()

if re.search("@", email):
    print("Valid")
else:
    print("invalid")


# .      any character except a newline
# *      0 or more repetitions
# +      1 or more repetitions
# ?      0 or 1 repetitions
# {m}    m repetitions
# {m,n}  m-n repetitions
# ^      matches the start of the string
# $      end of the string 
# \      escape character - voglio che finisca con (.edu)
# []     set of characters
# [^]    complementing set , set di ogni carattere da escludere

import re

email = input("Whats ur email? ").strip()

if re.search(".+@.+", email):
    print("Valid")
else:
    print("invalid")

# introduzione a (r"...")

import re

email = input("Whats ur email? ").strip()

if re.search(r".+@\.edu", email):   # raw string "r" per re.search
    print("Valid")
else:
    print("invalid")      # Controlla che indica una raw string (così Python non interpreta \ come carattere speciale)

# Nel contesto dell’if, significa:
#      Se trova una corrispondenza → la condizione è vera
#      Se non trova nulla → la condizione è falsa


# Inserendo altre str nell input cosi il programma lo riconosca

import re

email = input("Whats ur email? ").strip()

if re.search(r"^.+@.+\.edu$", email):  
    print("Valid")
else:
    print("invalid") 


# Modificando in modo che non accetti altri simboli in eccesso
# ^       inizio della stringa
# [^@]    significa: ogni carattere escluso @
# +       significa: 1 o piu elementi a sinistra
# +\.edu  significa: 1 o piu elementi e letteralmente .edu
# $       fine della stringa
import re

email = input("Whats ur email? ").strip()

if re.search(r"^[^@]+@[^@]+\.edu$", email): 
    print("Valid")
else:
    print("invalid") 


#--------------------------------------------------------------------------------

# modificando per uno standard mondiale -definizione di email-

# [a-zA-Z]         range di lettere(tutte) 
# [a-zA-Z0-9_]     range di lettere e numeri(tutti)
# - (hyphen)       sarebbe il trattino normale
# _                lo si mette per includerlo ( utilizzato nelle email)

import re

email = input("Whats ur email? ").strip()

if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email): 
    print("Valid")
else:
    print("invalid") 

# Shortcuts ------------------------------------------------
# \w         sarebbe word sulla tastiera: any word character
# \d         decimal digit
# \D         not decimal digit
# \s         whitespace characters  
# \S         not a whitespace characters
# \W         not a word character
# (edu|com|...)  either edu or com
# (...)          a group
# (?: ...)       non capturing version ( )
import re

email = input("Whats ur email? ").strip()

if re.search(r"^\w+@\w+\.(edu|com|gov|net|org)$", email):  
    print("Valid")
else:
    print("invalid") 


# Esempio di \w tutte la tastiera e/o \s spazi bianchi

import re

email = input("Whats ur email? ").strip()

if re.search(r"^(\w|\s)+@\w+\.edu$", email):  
    print("Valid")
else:
    print("invalid") 

# Gestendo maiuscole e minuscole nel dominio .edu (.EDU)
# inserendo 1 dei lower() mostrati 

# oppure usare : re.search(patter,string, flags= (questi sotto))
# re.IGNORECASE   ignora le maiuscole dell input utente
# re.MULTILINE    accetta multi linee come paragrafi ecc...
# re.DOTALL       configura che il "."  accetti tutti i caratteri anche new line
import re

email = input("Whats ur email? ").strip()#.lower()

if re.search(r"^\w+@\w+\.edu$", email, re.IGNORECASE):  # email.lower()
    print("Valid")
else:
    print("invalid") 


# per rendere il Sub-Dominio opzionale :

import re

email = input("Whats ur email? ").strip()

if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email):  
    print("Valid")
else:
    print("invalid") 



# Un altra libreria per convaòidare ufficialmente una email
# re.match(pattern, string, flag = 0)
# Creo un altro file: format.py

name = input("Whats your name? ").strip()
if "," in name:
    last, first = name.split(", ")
    name= f"{first} {last}"
print(f'hello, {name}')


# Come rendere la separazione della "," opzionale 

import re

name = input("Whats your name? ").strip()
matches = re.search(r"^(.+), (.+)$", name)  # per catturare il nome e cognome
if matches:
    last = matches.group(1)
    first = matches.group(2)
    name = f"{first} {last}"
print(f"hello, {name}")

# POI diventa :
import re

name = input("Whats your name? ").strip()
matches = re.search(r"^(.+), (.+)$", name)  # per catturare il nome e cognome
if matches:
    name= matches.group(2) + " " + matches.gropus(1)
print(f"hello, {name}")


# Pulizia del codice

import re

name = input("Whats your name? ").strip()
if matches := re.search(r"^(.+), *(.+)$", name) :
    name = matches.group(2) + " " + matches.gropus(1)
print(f"hello, {name}")


# :=  Walrous Operator  ( tricheco )
#
# sarebbe la combinazione di if e = quindi := e non == 



# estrapolare un informazione specifica: user name only 
# esempio con https://twitter.com/

url = input("URL: ").strip()

username = url.replace("https://twitter.com/", "") # replace(dai argomento vecchio,dai nuovo argomento)

# Prefiss remove - quale stringa o sub stringa vuoi rimuovere? 

url = input("URL: ").strip()

username = url.removeprefix("https://twitter.com/")

#--------------------------------------------------------------------
# re.sub( pattern, repl, string, count=0, flag=0 )

import re

url = input( "URL: ").strip()

username = re.sub(r"https://twitter.com/", "", url)
print(f"Username: {username}")

# Aggiungere simboli per restringere il campo

import re

url = input( "URL: ").strip()

username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
print(f"Username: {username}")


#################  RECAP  ##########################################################################

import re

url = input( "URL: ").strip()

if matches := re.search(r"^https?://(?:www\.)?twitter\.com/(.+)$", url, re.IGNORECASE):
    print(f"Username:", matches.group(1))


# importo la libreria

# ottengo url dall'utente

# cerco nell'Url dell'utente , come indicato nel secondo argomento ", url,"
# la espressione regolare: ^https?://(www\.)?twitter\.com/(.+)$

# if: se ho il match di quel che cerco= ricevo l'username

# Group(1) si riferisce al primo () perche ci interessa username, non il pre dominio

# := Walrus  : Assignment Expression
# Permette di assegnare un valore a una variabile mentre lo usi in un espressione
# Variabile := Espressione
lista= []

n = len(lista)
if n > 10:
    print(n)

# con walrus

if (n := len(lista)) > 10 :
    print(n)

# Nei cicli While

line = input()
while line != "":
    print(line) 
    line = input()

# con walrus

while (line := input()) != "":
    print(line)

# Liste comprehension

numeri = [1,2,3,4]

risultato = [n for x in numeri if (n := x *2) >4]
print(risultato)


# se voglio rendere opzionale .com e inserire altri domini tipo .org ecc... , 
# ma con if chiarifico che passa solo .com

import re

url = input( "URL: ").strip()

if matches := re.search(r"^https?://(?:www\.)?twitter\.(.+)/(.+)$", url, re.IGNORECASE):
    if matches.group(1) == "com":
        print(f"Username:", matches.group(1))


# FINALE: -----------------------------------------------------------------------------------------------------------------------

import re

url = input( "URL: ").strip()

if matches := re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)", url, re.IGNORECASE):
    print(f"Username:", matches.group(1))
