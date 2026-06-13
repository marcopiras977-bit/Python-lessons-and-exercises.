# Esercizio 1:


numeri = [12, 5, 8, 21, 3, 18]

def analizza_numeri(numeri):
    risultato = {
        "pari": 0,
        "dispari": 0,
        "somma": 0
    }

    for i in numeri:
        risultato["somma"] += i

        if i % 2 == 0:
            risultato["pari"] += 1
        else:
            risultato["dispari"] += 1

    return risultato


print(analizza_numeri(numeri))


# Esercizio 2:

macchine = {
    "M1": 45,
    "M2": 90,
    "M3": 30,
    "M4": 100
}

def stato_macchine(macchine):
    risultato = {}

    for nome, temp in macchine.items():
        if temp > 80:
            risultato[nome] = "ALLARME"
        else:
            risultato[nome] = "OK"

    return risultato


print(stato_macchine(macchine))


# Esercizio 3:

numeri = [4, 9, 15, 2, 7, 18]

i = 0
massimo = numeri[0]

while i < len(numeri):
    if numeri[i] > massimo:
        massimo = numeri[i]
    i += 1

print(massimo)  


# Esercizio 

numeri = [2, 5, 8, 3, 10, 7, 4]

# Vogliamo trasformarla in un dizionario che conta:

# quanti numeri sono pari

# quanti sono dispari

risultato = {
    "pari": 0,
    "dispari": 0
}

# Prima del ciclo For , dobbiamo decidere dove mettere i risultati
# Usando dei contatori

for n in numeri: 
    if n % 2 == 0:
        risultato["pari"] += 1
    else:
        risultato["dispari"] += 1

# Riassunto: 
# 1. Creo dizionario con contatori 
# 2. Faccio ciclo
# 3. Aggiorno valori
# 4. Return dizionario

numeri = [2, 5, 8, 3, 10, 7, 4]

def conta_pari_dispari(numeri):
    risultato = {
        "pari": 0,
        "dispari": 0
    }

    for n in numeri:
        if n % 2 == 0:
            risultato["pari"] += 1
        else:
            risultato["dispari"] += 1

    return risultato

print(conta_pari_dispari(numeri))
# # # # # # # # # # # # # # # # # # # # # # #


# Per appendere / salvare i numeri di una lista in un dizionario : 
numeri = [2, 5, 8, 3, 10, 7, 4]

def lista(numeri):
    risultato = {
        "pari": [],
        "dispari": []
    }

    for n in numeri:
        if n % 2 == 0:
            risultato["pari"].append(n)    # perche posso aggiungere n ad una lista presente nel dizionario creato prima
        else:
            risultato["dispari"].append(n)

    return risultato

print(lista(numeri))  

# lista.append(valore)
# --------------------------------------------------------------------------- 
# calcola somma totale, trova numero piu grande, conta quanti sono pari
numeri = [7, 2, 9, 4, 1, 8]

def analizza(numeri):
    diz = {
        "somma": 0,
        "massimo": [],
        "pari": 0
    }

    for n in numeri:
        if n % 2 == 0:
            diz["pari"] += 1
        
        if n > n-1:                 # Ho scritto che la condizione è vera...
            diz["massimo"].append(n) # Devo correggere nel diz ("massimo": numeri[0])
                                    # Poi if n > diz["massimo"]: diz["massimo"] = n
        
        diz["somma"] += n

    return diz

print(analizza(numeri))

# Quindi #

numeri = [7, 2, 9, 4, 1, 8]

def analizza(numeri):
    diz = {
        "somma": 0,
        "massimo": numeri[0],
        "pari": 0
    }

    for n in numeri:
        diz["somma"] += n

        if n % 2 == 0:
            diz["pari"] += 1

        if n > diz["massimo"]:
            diz["massimo"] = n

    return diz

print(analizza(numeri))
#
# input -> logica -> output

