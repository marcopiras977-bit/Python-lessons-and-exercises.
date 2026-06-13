# Dizionari 

# con i dizionari puoi immagazzinare piu valori (2) (key)

#dict = {key: value, key: value}  # key: value tutto questo è solo un valore 

actions = {"r": 1,"l":-1}
print(actions)

# Per estrapolare dal dizionario un valore usando le liste
print(actions["r"])   # 1

# Azione .get invece di estrapolare una cosa che non c'è ( e dovrebbe darti l'errore ) invece ti dice NONE

# per cambiare il valore in un dizionario
actions["r"] = 2

# per aggiungere un valore al dizionario
actions["u"] = 3

# per in output keys,valori e oggetti :
print(actions.keys())    # lista delle keys
print(actions.values())  # lista dei valori delle keys
print(actions.items())   # Lista di tuples (keys e valori)

# rimuovere usando del(), remove(), .pop() 
# del() : eliminare una items 
del(actions["u"])  

# .pop funzione toglie il valore e la key dal dizionario
actions.pop("r")

# In operator Determina se esiste quella cosa nel dizionario
print("l" in actions) 
# risposta sarà True o False

# Dizionari / Recap

actions = {"r":1 , "l":2}    # creazione del Dizionario, poi print.
print(actions["r"])          # per prendere dal dizionario un valore
actions["r"] = 3             # per cambiare un valore nel dizionario
actions["u"] = 6             # per aggiungere un valore al dizionario
del(actions["u"])          # per eliminare una items dal dizionario
actions.pop("r")           # per togliere un valore e la key dal dizionario 
print(actions.keys())       # per printare la lista delle keys
print(actions.values())     # per printare la lista dei valori delle keys  
print(actions.items())      # per printare la lista di tuples (keys e valori)
print("l" in actions)      # per verificare se esiste quella cosa nel dizionario (True/False)

# spacecraft funzione con dizionari----------------------------------------------------------------------

def main():
    spacecraft = { "name" : "Voyager 1", "distance": 163}
    print(create_report(spacecraft))
# Aggiungere una key
    spacecraft["distance"] = 0.01 


def create_report(spacecraft):
    return f'''
    ========= Report ========

    Name : {spacecraft["name"]}
    Distance : {spacecraft["distance"]} AU 

    =========================
    '''

main()

# .get evita che ti dia lerrore se immetti "Unknown". 
# es. Distance: {spacecraft.get("distance", "Unknown")}
# output ,se distance non esiste, Unknown 

# Aggiungere oggetto al dizionario
    # spacecraft.update({"distance": 0.01,"orbit" : "Sun"})

distances = {
    "Voyager 1 ": 163,
    "Voyager 2 ": 136,
    "Pioneer 10 ": 80,
    "New Horizon ": 58,
    "Pioneer 11 ": 44
}

def main():
    for name in distances.keys():  # prende il nome delle keys.
        print(f'{name}is {distances[name]}')

def convert(au):
    return au * 149597870700

main()

def main():
    for distance in distances.values():  # prende il nome delle keys.
        print(f'{distance} AU is {convert("distance")} m')

def convert(au):
    return au * 149597870700

main()