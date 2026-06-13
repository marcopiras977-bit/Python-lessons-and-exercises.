# inheritance 
# classi e oggetti 

class GameObject:

    def __init__(self, name, x_pos, y_pos):
        self.name = name
        self.x_pos = x_pos
        self.y_pos = y_pos
    
    def move(self, by_x_amount, by_y_amount):
        self.x_pos += by_x_amount
        self.y_pos += by_y_amount

game_object = GameObject("enemy", 1, 2)

# un inheritance è Creare una nuova classe che contenga tutte le cose di una classe , ma con proprie caratteristiche
# super classe e una sub classe 

class GameObject:

    def __init__(self, name, x_pos, y_pos):
        self.name = name
        self.x_pos = x_pos
        self.y_pos = y_pos
    
    def move(self, by_x_amount, by_y_amount):
        self.x_pos += by_x_amount
        self.y_pos += by_y_amount

class enemy(GameObject):

    def __init__(self, name , x_pos, y_pos, health):
        super().__init__(name, x_pos, y_pos)           # super() serve a richiamare la funzione 
        self.health = health                           # super() ti permette di riusae metodi e attributi dalla classe "genitore" senza riscriverli

    def take_damage(self,amount):
        self.health -= amount


game_object = GameObject("enemy", 1, 2)

enemy = enemy("enemy",5 ,10 ,100)
print(game_object.name)
print(enemy.name)   
enemy.take_damage(20)
print(enemy.health)



# ESEMPIO DI SUPER()

class animale:
    def __init__(self, nome):
        self.nome = "Doggo"

        def parla(self):
            print("L'animale da un verso")

# classe figlia senza super()

class Cane(animale):
    def __init__(self, nome,razza):
        self.nome = "Doggo"
        # dobbiamo riscriverlo
        self.razza = "argentino"

# Utilizzando super() 

class Cane( animale):
    def __init__(self, nome, razza):
        super().__init__(nome)
        # chiama __INIT__ della classe animale
        self.razza = "argentino"

# cosi non ripeti il codice e se cambi genitore , funziona ancora

