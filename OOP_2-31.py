# OOP 2.py

class Student:                 # inizializzando la classe,il contenuto dell Oggetto 
    def __init__(self,name,house):
        self.name = name
        self.house = house

def main():
    student = get_student()
    print(f"{student.name} from {student.house}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    student = Student(name, house)
    return student

if __name__ == "__main__ ":
    main()


# Incapsulazione della Classe / raise Error (Eccezioni)

class Student:                 
    def __init__(self,name,house):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "hufflepuff", "Ravencalw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house

def main():
    student = get_student()
    print(f"{student.name} from {student.house}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__ ":
    main()


# locazione dell'oggetto nella memoria del computer

class Student:                 
    def __init__(self,name,house):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "hufflepuff", "Ravencalw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house

def main():
    student = get_student()
    print(student)           # output la posizione specifica del oggetto nella memoria del PC

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__ ":
    main()


# Metodo Speciale __str__ 

class Student:                 
    def __init__(self,name,house):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "hufflepuff", "Ravencalw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"        # output __str__ prende loggetto e lo riporta all output,circa

def main():
    student = get_student()
    print(student)                                     # funziona solo se c'è __str__ 

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__ ":
    main()


# Inserendo altri dati (Patronus)

class Student:                 
    def __init__(self,name,house,patronus):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "hufflepuff", "Ravencalw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house
        self.patronus = patronus

    def __str__(self):
        return f"{self.name} from {self.house}"
         
def main():
    student = get_student()
    print(student)

def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    return Student(name, house, patronus)


if __name__ == "__main__ ":
    main()


# inventando una funzione ("charm" va sempre inizializzato con self,per accedere alloggetto Student)

class Student:                 
    def __init__(self,name,house,patronus):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "hufflepuff", "Ravencalw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house
        self.patronus = patronus

    def __str__(self):
        return f"{self.name} from {self.house}"
        
    def charm(self):
        match self.patronus:
            case "Stag":
                return ""  # ci va un emoji 
            case "Otter":
                return ""  # ci va un emoji 
            case "Jack Russell terrier":
                return ""  # ci va un emoji
            case _:
                return ""  # ci va un emoji ( uscirà nel caso non verrà riconosciuta)


def main():
    student = get_student()
    print("Expecto Patronum!")
    print(student.charm())   # Richiama la funzione charm()

def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    return Student(name, house, patronus)


if __name__ == "__main__ ":
    main()


# Properties : funzionalità di evitare di fare casini nelle classi-------------
# @property  === decorators
class Student:                 
    def __init__(self,name,house):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "hufflepuff", "Ravencalw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"
        
def main():
    student = get_student()
    print(student)

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__ ":
    main()


# 