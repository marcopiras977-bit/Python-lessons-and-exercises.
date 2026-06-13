# Basi funzioni com PyMike su youtube ( Le Funzioni .11 )

#def function(x):
    #return x * x
#print(func(x))

def say_my_name():       #interno della parentesi vanno i parametri,Ma NON Sempre serve
    name = input("Come ti chiami? ")
    print("Il tuo nome è ", name)
    
say_my_name()


# Funzioni: richiamo funzioni

# Serve a creare blocchi di codice ripetibile; serve a scegliere esattamente quando e dove usare il codice
# def function_name():

position = 0

def move_player():    # global position = serve per usare variabili fuori dalla funzione.
    global position
    position += 1
    print(position)

move_player()         # Devi richiamare la funzione, se no non funziona. E puoi ripetere la funzione quante volte vuoi

# Global funzione = serve per usare variabili fuori dalla funzione. 
# es. x = 10 ; def aumenta(): global x , x = x + 1 ; aumenta() ; print(x) 
# COMUNQUE NON SI USA MOLTO , SOLO PER PICCOLE COSE, CODICI

# Temporali variabili parametri

position = 0

def move_player(by_amount):
    global position
    position += by_amount 
    print(position)

move_player(5)    # output sarà 5 

# Inserisco altre variabili / parametri 

position = 0

def move_player(position, by_amount):           # position e by_amount sono parametri
    position += by_amount
    print(position)

move_player(position, 5)                        # output : 5 (perche position è 0 )

# RETURN = serve a dare un output alla funzione, stesso discorso di Print ma strutturato in un momentaneo modo.
# IMPORTANTE: quando il codice arriva a return ti da L'output ma tutto quello scritto dopo (NELLA STESSA FUNZIONE) non verrà eseguito

position = 0

def move_player(position, by_amount):           # position e by_amount sono parametri
    position += by_amount
    return position

position = move_player(position, 5) 
print(position)
position = move_player (position, 2)
print(position)
# Se aggiungo : position = move_player( position, 2) ,in uscita mi darà la somma aggiornata quindi 7!
