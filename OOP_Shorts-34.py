# Classes

class Package:
    def __init__(self, number, sender, recipient, weight): # attributi
        self.number = number
        self.sender = sender                    # Variabili d'istanza
        self.recipient = recipient
        self.weight = weight

# Accesso alla classe 
def main():
    packages =[
        Package(number = 1, sender = "Alice", recipient = "Bob", weight = 10),
        Package(number = 2, sender = "Bob", recipient = "Charlie", weight = 5)
    ]


main()


# --------------------Class methods and Variables---------------------

class Food:
    def __init__(self, ingredients):
        self.ingredients = ingredients
        self.hearts = Food.calculate_hearts(ingredients)
    
    @classmethod # dice a python che questa funzione è in metodo di classe 
    def calculate_hearts(cls, ingredients):
        hearts = 1 
        for ingredient in ingredients:
            if "hearty" in ingredient.lower():
                hearts += 2
            else:
                hearts += 1
        return hearts


def main():
    mushroom_skewer = Food(ingredients=["Mushroom","Hearty Mushroom"])
    print(f"This skewer heals {mushroom_skewer.hearts} hearts")

main()

# class variable

class Food:
    base_hearts = 1 # class variable

    def __init__(self, ingredients):
        self.ingredients = ingredients
        self.hearts = Food.calculate_hearts(ingredients)
    
    @classmethod # dice a python che questa funzione è in metodo di classe 
    def calculate_hearts(cls, ingredients):
        hearts = cls.base_hearts # cls è la classe food, prendo class variable
        for ingredient in ingredients:
            if "hearty" in ingredient.lower():
                hearts += 2
            else:
                hearts += 1
        return hearts


def main():
    mushroom_skewer = Food(ingredients=["Mushroom","Hearty Mushroom"])
    print(f"This skewer heals {mushroom_skewer.hearts} hearts")

main()

# I metodi di classe sono utili per la funzioanlità che devono essere condivise tra tutte 
# le istanze della tua classe. 
# sono utili per incorporare informazioni sulla classe stessa
# e per accedervi tramite il nome della classe, senza legarle a nessuna istanza particolare.

class Food:
    base_hearts = 1 

    def __init__(self, ingredients):
        self.ingredients = ingredients
        self.hearts = Food.calculate_hearts(ingredients)
    
    @classmethod 
    def calculate_hearts(cls, ingredients):
        hearts = cls.base_hearts 
        for ingredient in ingredients:
            if "hearty" in ingredient.lower():
                hearts += 2
            else:
                hearts += 1
        return hearts
    
    @classmethod                # creo una nuova istanza della classe Food,sovrascritto alcuni valori predefiniti
    def from_nothing(cls,hearts):
        food = cls(ingredients=[])
        food.hearts = hearts     # valori sovrascritti
        return food

def main():
    mushroom_skewer = Food(ingredients=["Mushroom","Hearty Mushroom"])
    print(f"This skewer heals {mushroom_skewer.hearts} hearts")

    # find some food 

    mushroom_skewer = Food.from_nothing(hearts=2)
    print(f"This skewer heals {mushroom_skewer.hearts} hearts")

main()


# ---------------------------- Instance Variable --------------------------------

class Package:
    def __init__(self, number, sender, recipient, weight): # attributi / inputs
        self.number = number
        self.sender = sender                    # Variabili d'istanza
        self.recipient = recipient
        self.weight = weight

# Accesso alla classe 
def main():
    packages =[
        Package(number = 1, sender = "Alice", recipient = "Bob", weight = 10),
        Package(number = 2, sender = "Bob", recipient = "Charlie", weight = 5)
    ]


main()

# iterando nella classe / accesso alle variabili istanza

class Package:
    def __init__(self, number, sender, recipient, weight): # attributi
        self.number = number
        self.sender = sender                    # Variabili d'istanza
        self.recipient = recipient
        self.weight = weight

# Accesso alla classe 
def main():
    packages =[
        Package(number = 1, sender = "Alice", recipient = "Bob", weight = 10),
        Package(number = 2, sender = "Bob", recipient = "Charlie", weight = 5)
    ]
    for package in packages:
        print(package.number)     # output 1 \n 2 
        print(f"Package {package.number}: {package.sender} to {package.recipient},{package.weight} kg")

main()


# ------------------------- Metodi di Istanza ----------------------------------

class Package:
    def __init__(self, number, sender, recipient, weight): 
        self.number = number
        self.sender = sender                    
        self.recipient = recipient
        self.weight = weight

    def __str__(self):
        return "This is a package."


def main():
    packages =[
        Package(number = 1, sender = "Alice", recipient = "Bob", weight = 10),
        Package(number = 2, sender = "Bob", recipient = "Charlie", weight = 5)
    ]
    for package in packages:     
        print(package) # accesso alla memoria posizione in memoria (SENZA __str__)

main()        # Output (CON __str__ : This is a package)

# Incapsulare 

class Package:
    def __init__(self, number, sender, recipient, weight): 
        self.number = number
        self.sender = sender                    
        self.recipient = recipient
        self.weight = weight

    def __str__(self):
        return f"Package {self.number}: {self.sender} to {self.recipient}, {self.weight} kg"


def main():
    packages =[
        Package(number = 1, sender = "Alice", recipient = "Bob", weight = 10),
        Package(number = 2, sender = "Bob", recipient = "Charlie", weight = 5)
    ]
    for package in packages:     
        print(package) # accesso alla memoria posizione in memoria (SENZA __str__)

main()        # Output (CON __str__ : darà output quello che hai messo in def main())


# Aggiungere funzionalità al metodo / prezzo per kg 

class Package:
    def __init__(self, number, sender, recipient, weight): 
        self.number = number
        self.sender = sender                    
        self.recipient = recipient
        self.weight = weight

    def __str__(self):
        return f"Package {self.number}: {self.sender} to {self.recipient}, {self.weight} kg"

    def calculate_cost(self, cost_per_kg):
        return self.weight * cost_per_kg


def main():
    packages =[
        Package(number = 1, sender = "Alice", recipient = "Bob", weight = 10),
        Package(number = 2, sender = "Bob", recipient = "Charlie", weight = 5)
    ]
    for package in packages:     
        print(f"{package} costs ${package.calculate_cost(cost_per_kg=2)}") 

main()       

  