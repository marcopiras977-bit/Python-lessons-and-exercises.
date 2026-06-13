# Collezioni : Liste 

# Liste
nome_lista = [5, True, "string"] # Qualsiasi cosa,quanto ne voglio, puo essere VUOTA
enemy_position = [5, 10 ,15]
print (enemy_position)

# indice 0, 1, 2, 3, ...
print(enemy_position[0])
print(enemy_position[1])

# lunghezza lista 
print(len(enemy_position))

# Se voglio cambiare 1 numero dalla lista :
enemy_position[0] = 6
print(enemy_position)  # [5->6 , 10 , 15]

# Se voglio print i primi due oggetti dalla lista : (:)
print(enemy_position[0:2])  # dal primo (0) al (:) secondo (2)

# Append function --- aggiunge un valore alla lista
enemy_position.append(25)
print(enemy_position)

# insert function --- aggiunge, specificando la posizione, un oggetto 
enemy_position.insert(1,9)   # nel posto 1 aggiungi 9 
print(enemy_position)

# remove function --- rimuovere uno specifico oggetto 
enemy_position.remove(6)
print(enemy_position)

# Delete function --- eliminare un oggetto 
del(enemy_position[2])      # elimina l'oggetto usando la sua posizione
print(enemy_position)


# Lista / Recap

enemy_position = [5, 10 ,15]  # lista creata
print(len(enemy_position))    # lunghezza lista
print(enemy_position[0])      # primo oggetto
enemy_position[0] = 6         # cambiare il primo oggetto
print(enemy_position[0:2])    # print i primi due oggetti
enemy_position.append(25)     # aggiungere un oggetto alla lista
enemy_position.insert(1,9)    # aggiungere un oggetto specificando la posizione, quindi nel posto 1 aggiungi 9
enemy_position.remove(6)      # rimuovere un oggetto specifico
del(enemy_position[2])        # eliminare un oggetto usando la sua posizione
print(enemy_position)         # print lista finale


numeri = [3, 10, 5, 8, 2, 7]

def numeri_doppi(numeri):
    lista= []
    for n in numeri:
        if n > 5:
            numeri_molt = n * 2
            lista.append(numeri_molt)
    return lista

# list comprehension

#[<espressione> for <elemento> in <iterabile> if <condizione> else <altrimenti>]

numeri = [3, 10, 5, 8, 2, 7]

lista = [n * 2 for n in numeri if n > 5]


##### Liste #####
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
results = ["Mario","luigi"]

results.append("Princess")
results.append(["Bowser","Donkey Kong"]) #Stampa con le parentesi quadre,dentro la lista
results.extend(["Bowser","Donkey Kong"]) #Stampa senza le parentesi,dentro la lista
results.remove("Bowser") # Rimuove Bowser
results.insert(0,"Bowser")# inserisce al posto 0,sarebbe il primo,Bowser
results.reverse() #Inverte la lista

print(results)

############ List Methods #############

def main():
    history = []

    while True:
        action = input("Action: ")

        if action == "Undo":
            undone = history.pop()    # Tolgo le azioni, se inserisco Undo
            print(f'"Undone: {undone}')
        elif action == "Restart":
            history.clear()          # con Restart rimuove tutta la lista
        else:
            history.append(action)   # Aggiungo le azioni
        print(history)


main()

lista = [1, 2]
lista.append(3)

print(lista)

# output : [1,2,3]

lista = [1, 2]
lista.append([3, 4])
print(lista)

# output : [1, 2, [3, 4]]

lista = [1, 2]
lista += [3, 4]
print(lista)

# output : [1, 2, 3, 4]

lista = [1, 2]
lista += "ciao"
print(lista)

# output : [1, 2, 'c', 'i', 'a', 'o']

