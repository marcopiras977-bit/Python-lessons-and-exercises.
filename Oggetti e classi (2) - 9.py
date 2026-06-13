# Oggetti e classi  - parte 2

# qualsiasi cosa aggiungi senza self. non appartiene alla funzione __init__

class GameObject:

    def __init__(self, name, x_pos, y_pos):
        self.name = name
        self.x_pos = x_pos
        self.y_pos = y_pos

game_object = GameObject("enemy", 1, 2)
print(game_object.name)
game_object.name = "enemy 1"                 
print(game_object.name)                      # OUTPUT : enemy ; enemy 1

print(game_object.x_pos)
print(game_object.y_pos)

# non posso aggiungere game_object.damage = 5 Perche non esiste nella funzione, ancora

# Aggiungo una funzione per il movimento :
class GameObject:

    def __init__(self, name, x_pos, y_pos):
        self.name = name
        self.x_pos = x_pos
        self.y_pos = y_pos
    
    def move(self, by_x_amount, by_y_amount):
        self.x_pos += by_x_amount
        self.y_pos += by_y_amount

game_object = GameObject("enemy", 1, 2)
print(game_object.name)
game_object.name = "enemy 1"                 
print(game_object.name)                      # OUTPUT : enemy ; enemy 1.

print(game_object.x_pos)
print(game_object.y_pos)

game_object.move(5, 10 )
print(game_object.x_pos)
print(game_object.y_pos)                     # OUTPUT : enemy ; enemy 1; 2; 6; 12.

# Posso creare quanti game_object io voglio: ( Cambiando ovviamente la variabile )

other_game_object = GameObject("Player", 2, 0) 
print(other_game_object.name) 
print(other_game_object.x_pos)
print(other_game_object.y_pos)

one_int = 5
another_int= one_int 
print(one_int)
print(another_int)

