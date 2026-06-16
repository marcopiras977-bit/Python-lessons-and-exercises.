# For in Loop 

# FOR item IN collection:
    # execute code using that item 

# A 'for in' loop is used to execute code a set number of times only!!!!!

enemy_position = [5, 10 , 15]

for enemy_position in enemy_position:    # 5 , 10 , 15 pero in colonna,non in fila
    print(enemy_position)

# Range() ripete quante volte inserito il print.
for i in range(0, 5):
    print("Hello")
# stampa Hello 5 volte , perche range(0,5) significa da 0 a 4 , quindi 5 volte in totale
for i in range(0, 10, 2):  # il 2 è l'incremento
    print(i)
# stampa 0,2,4,6,8 perche range(0,10,2) significa da 0 a 9 con incremento di 2

# For In Loop / Recap
enemy_position = [5, 10 , 15]   # lista creata
for enemy_position in enemy_position:    # per ogni oggetto nella lista , printa l
    print(enemy_position)          # l'oggetto
for i in range(0, 5):            # ripeti 5 volte
    print("Hello")               # stampa Hello 5 volte
for i in range(0, 10, 2):       # da 0 a 9 con incremento di 2
    print(i)                    # stampa i





# For loops HarvardX

def main():
    print(write_letter("Mario", "Princess Peach"))
    print(write_letter("Luigi", "Princess Peach"))
    print(write_letter("Daisy", "Princess Peach"))
    print(write_letter("Yoshi", "Princess Peach"))

def write_letter(receiver, sender): # argument / parametri da definire (receiver, sender)
    return f'''
------------------------------------
 Dear {receiver},
 you are cordially invited to a ball at
 Peach's Castle this evening,7:00 PM.

 Sincerely,
 {sender}
------------------------------------
'''

main()

################## Migliorare il codice:##################################

def main():
    names = ["Mario","Luigi","Daisy","Yoshi"]
    for i in range(len(names)): # ritorna i numeri degli oggetti nella lista con len (ritorna i numeri ) usando la lista names e inserendo [i] trasform in stringhe
        print(write_letter(names[i], "Princess Peach"))

def write_letter(receiver, sender): # argument / parametri da definire (receiver, sender)
    return f'''
------------------------------------
 Dear {receiver},
 you are cordially invited to a ball at
 Peach's Castle this evening,7:00 PM.

 Sincerely,
 {sender}
------------------------------------
'''

main()

################# Migliorarlo ancora ############################à

def main():
    names = ["Mario","Luigi","Daisy","Yoshi"]
    for name in names: # ritorna tutti i nomi della lista
        print(write_letter(name, "Princess Peach"))

def write_letter(receiver, sender): # argument / parametri da definire (receiver, sender)
    return f'''
------------------------------------
 Dear {receiver},
 you are cordially invited to a ball at
 Peach's Castle this evening,7:00 PM.

 Sincerely,
 {sender}
------------------------------------
'''

main()
