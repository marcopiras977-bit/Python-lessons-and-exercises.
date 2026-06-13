# Class Methods # hat.py # cappello di sorteggio harry potter

#class Hat:
    #...

# hat = Hat() # istanzio un oggetto / sintassi comune per istanziare un oggetto di una classe 
# hat.sort("Harry") # decido di supporre che da output in quale casa dovrebbe essere quello studente


# Incapsulazione nella Classe Hat
import random

class Hat:
    def __init__(self):   # ho definito l'inizializzazione dell'oggetto che memorizza la lista delle casate,cosi non devo riscriverla ogni volta
        self.houses  = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
    def sort(self,name):  # con sort() accedo alla lista, ma random
        print(name, "is in" , random.choice(self.houses))
        
hat = Hat()
hat.sort("Harry")   # Output = una scelta random delle case per Harry


# @classmethod = A class method receives the class as implicit first argument,just like an instance method receives the instance.
# @classmethod = variabili della classe stessa 
import random

class Hat:

    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    @classmethod
    def sort(cls, name):  
        print(name, "is in" , random.choice(cls.houses))
        
Hat.sort("Harry")  # Sto solo accedendo a un metodo di classe all'interno della classe hat
# Output = una scelta random delle case per Harry


# Funziona anche cosi:

import random

houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

def sort(name):  
        print(name, "is in" , random.choice(houses))
        
sort("Harry")  # Output = una scelta random delle case per Harry


# Ripresa di un esercizio e spiegazione :

class Student:                 
    def __init__(self,name,house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"


def main():
    student = get_student()
    print(student)

def get_student():            # funzione che ti "aiuta" a ricevere uno studente.
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__ ":
    main()



# inserendo get_student() => get(cls) facendola diventare da funzione a classmethod
# crea automaticamente uno studente dentro la classe (supporta l'ereditarietà, ecc...)

class Student:                 
    def __init__(self,name,house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)      # significa return Studente(name, house)

def main():
    student = Student.get()          # significa che dalla classe Student deve ricevere e dare output uno studente
    print(student)


if __name__ == "__main__ ":
    main()


#-----------------------------------------------------------------------------
# Static Method   @staticmethod
# inheritance / ereditarietà 
class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name

class Student:                 
    def __init__(self,name,house):
        if not name:
            raise ValueError("Missing name")
        self.name = name
        self.house = house

class Professor:
    def __init__(self,name,subject):
        if not name:
            raise ValueError("Missing name")
        self.name = name
        self.subject = subject

# Per non ripetere il codice in 2 o piu classi :

class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name

class Student(Wizard):                 
    def __init__(self,name, house):
        super().__init__(name)
        self.house = house

class Professor(Wizard):
    def __init__(self,name,subject):
        super().__init__(name)
        self.subject = subject

wizard = Wizard("Albus")
student = Student("Harry", "Gryffindor")
professor = Professor("Severus","Defense Against the Dark Arts")


# ---------------------------------------------------------------------
# operator overloading  == es. + significa + e anche str + str e anche Regex ecc..
# vault.py // Bank Harry Potter 

class Vault:
    def __init__(self, galleons=0, sickles=0, knuts=0 ):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts

    # Senza __str__ da output il codice in memoria : 
    def __str__(self):    # definisco la cassaforte che venga stampata come stringa
        return f"{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts"


potter = Vault(100, 50, 25)
print(potter)

weasley = Vault(25, 50, 100)
print(weasley)

galleons = potter.galleons + weasley.galleons
sickles = potter.sickles + weasley.sickles
knuts = potter.knuts + weasley.knuts

total = Vault(galleons, sickles, knuts)
print(total)

# Alternativa per scrivere meno codice //  object.__add__(self, other)

class Vault:
    def __init__(self, galleons=0, sickles=0, knuts=0 ):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts
 
    def __str__(self):
        return f"{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts"

    def __add__(self, other):
        galleons = self.galleons + other.galleons
        sickles = self.sickles + other.sickles
        knuts = self.knuts + other.knuts
        return Vault(galleons, sickles, knuts)

potter = Vault(100, 50, 25)
print(potter)

weasley = Vault(25, 50, 100)
print(weasley)

total = potter + weasley
print(total)

#