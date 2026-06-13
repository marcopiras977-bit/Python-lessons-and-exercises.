# RANDOM
# Il modulo random fornisce funzioni per generare numeri casuali e per selezionare elementi casuali da una sequenza.

import random 

cards = ["jack", "queen", "king"]

def main():
    print(random.choice(cards))    # scelta casuale di un elemento da una lista
    print(random.choices(cards, k=2))  # scelta casuale di più elementi da una lista, con k che indica il numero di elementi da scegliere
    print(random.choices(cards,weights= [100,0,0], k=2)) # scelta casuale di più elementi da una lista, con k che indica il numero di elementi da scegliere e weights che indica la probabilità per ogni elemento
    print(random.sample(cards, k=2))   # scelta casuale di più elementi da una lista, senza ripetizioni, con k che indica il numero di elementi da scegliere
    print(random.randint(1,10))   # genera un numero intero casuale tra 1 e 10, inclusi entrambi gli estremi
    random.shuffle(cards)         # mescola la lista in modo casuale
    
main()
#----------------------------------------------------------------

def main():
    random.seed(0)  # imposta il seme per la generazione di numeri casuali, in modo da ottenere sempre gli stessi risultati
    random.seed(1)  # imposta un seme diverso per ottenere risultati diversi
    random.seed(2)  # imposta un seme diverso per ottenere risultati diversi
    print(random.choices(cards,k=2))


main()