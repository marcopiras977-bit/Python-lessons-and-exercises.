# Properties : funzionalità di evitare di fare casini nelle classi-------------
# @property  === decorators
# Getter e Setter impediscono a questo di sovrascrivere output,quindi di essere manipulato
# Per convenzione va messo _ per non far collidere le chiamate alla funzione e indica "Non toccare o modificare questa parte."
class Student:                 
    def __init__(self,name,house):
        if not name:
            raise ValueError("Missing name")
        self.name = name        # Variabile d'Istanza
        self.house = house      # Variabile d'Istanza

    def __str__(self):
        return f"{self.name} from {self.house}"
        
    # Getter = è una funzione per una classe che recupera alcuni attributi 
    @property
    def house(self):
        return self._house # Per convenzione va messo _ per non far collidere le chiamate alla funzione
    
    # Setter = è una funzione in una classe che imposta un certo valore
    # Verrà utilizzato da python ogni volta che verrà richiamato .house
    @house.setter
    def house(self,house):
        if house not in ["Gryffindor", "hufflepuff", "Ravencalw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house      # Per convenzione va messo _ per non far collidere le chiamate alla funzione


def main():
    student = get_student()
    student.house = "Number Four, Privet Drive"  # Getter e Setter impediscono a questo di sovrascrivere output,quindi di essere manipulato
    print(student)

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__ ":
    main()

# Getter e Setter permettono a Python di rilevare automaticamente quando stai cercando di impostare manualmente un valore

# Definendo Property anche per name

class Student:                 
    def __init__(self,name,house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"
        
    
    @property
    def name(self):
        return self._name
    
    @property
    def house(self):
        return self._house 
    
    @name.setter
    def name(self,name):
        if not name:
            raise ValueError("Missing Name")
        self._name = name

    @house.setter
    def house(self,house):
        if house not in ["Gryffindor", "hufflepuff", "Ravencalw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house      


def main():
    student = get_student()
    print(student)

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__ ":
    main()


# Modo piu pythonico di riscrivere questo sopra / 
# int è nelle documentazioni class int(x, base=10)
# str è nelle documentazioni class str(object='')
class Student:                 
    def __init__(self,name,house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"
        
    
    @property
    def name(self):
        return self._name
    
    @property
    def house(self):
        return self._house 
    
    @name.setter
    def name(self,name):
        if not name:
            raise ValueError("Missing Name")
        self._name = name

    @house.setter
    def house(self,house):
        if house not in ["Gryffindor", "hufflepuff", "Ravencalw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house      


def main():
    student = get_student()
    print(student)

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__ ":
    main()

