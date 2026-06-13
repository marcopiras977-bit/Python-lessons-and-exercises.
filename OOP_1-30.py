# Object-Oriented Programming

# student.py

name = input("Name: ")
house = input("House: ")
print(f"{name} from {house}")

# costruendo blocchi con funnzioni

def main():
    name = get_name()
    house = get_house()
    print(f"{name} from {house}")

def get_name():
    return input("Name: ")

def get_house():
    return input("House: ")

if __name__ == "__main__":
    main()


# creando get_student(): per riassumere quello scritto prima

def main():
    name ,house = get_student()
    print(f"{name} from {house}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return name, house

if __name__ == "__main__ ":
    main()


# Tuple datas # immutabile dati #
# se sbagli l'input esempio "Padme from Gryffindor" = TypeError : 'tuple' object does not support ...
# significa che quello inserito non è quello assegnato

def main():
    student = get_student()
    if student[0] == "Padma":
        student[1] = "Ravenclaw"
    print(f"{student[0]} from {student[1]}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return (name, house) #tupla

if __name__ == "__main__ ":
    main()

# usare lista invece di tupla

def main():
    student = get_student()
    if student[0] == "Padma":
        student[1] = "Ravenclaw"
    print(f"{student[0]} from {student[1]}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return [name, house] #Lista

if __name__ == "__main__ ":
    main()


# Usando il dizionario

def main():
    student = get_student()
    if student["name"] == "Padma":
        student["house"] == "Ravenclaw"
    print(f"{student['name']} from {student['house']}")

def get_student():
    name =  input("Name: ")
    house = input("House: ")
    return {"name": name, "house": house}

if __name__ == "__main__ ":
    main()


# Classes / Class ti permettono di inventare i tuoi tipi di dati e dargli un nome 
# docs.python.org/3/tutorial/classes.html

class Student:
    ...

def main():
    student = get_student()
    print(f"{student.name} from {student.house}")

def get_student():
    student = Student()
    student.name = input("Name: ")
    student.house = input("House: ")
    return student

if __name__ == "__main__ ":
    main()

# Crei la classe (class Student), memorizzi all'interno degli atributi(student.name ecc...)
# Accedi agli attributi (print(f"{student.name}from {student.house}"))


# Passando argomenti alla funzione.
# Methods : comportamenti delle funzioni...
# student = Student(name, house) si riferisce a ==> class Student e tutto quello che ce dentro
# Chiamato anche Costruttore

class Student:                 # inizializzando la classe
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
#