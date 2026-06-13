# OGGETTI E CLASSI

# gli Oggetti sono entita di codice con variabili e funzioni

name = "john"
age = 99
isZombie = False

# le Classi definiscono quali variabili e funzioni devono avere/essere 

class GameObject:

    def __init__(self, name, x_pos, y_pos):
        self.name = name
        self.x_pos = x_pos
        self.y_pos = y_pos

# ogni classe di quel oggetto ha una variabile di nome "name"; 

class GameObject:

    def __init__(self, name, x_pos, y_pos):
        self.name = name
        self.x_pos = x_pos
        self.y_pos = y_pos

game_object = GameObject("enemy", 1, 2)
print(game_object.name)
game_object.name = "enemy 1"                 # Per cambiare il nome ,in questo caso e mandarlo in output 
print(game_object.name)                      # NOTA : non cambia il nome, aggiunge un altro nome ( vedere output) 

