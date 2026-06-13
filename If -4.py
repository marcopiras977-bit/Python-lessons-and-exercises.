# Funzione if

# if condition = True , execute some code

key = "r"
if key == "r":
    print("move right")
elif key == "l":
    print("move left")
else:
    print("invalid Key")

print("done")

#esempio: pratica

key = input("inserisci una key: ")

if key == "":
    print("inserisci una key valida")

elif key == key.lower():
    print("Bravo")
else:
    print("ValueError")

# Esercizio find()

testo = "ciao"

if testo.find("z") == -1:
    print("non trovato") # find() restituisce -1 se non trova il carattere cercato

