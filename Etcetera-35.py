# Et Cetera

# -------------------------- set ---------------------------------

students = [
    {"name": "Hermione" , "house": "Gryffindor"},
    {"name": "Harry" , "house": "Gryffindor"},
    {"name": "Ron" , "house": "Gryffindor"},
    {"name": "Draco" , "house": "Slytherin"},
    {"name": "Padma" , "house": "Ravenclaw"}
]

houses = []
for student in students:
    if student["house"]not in houses:
        houses.append(student["house"])

for house in sorted(houses):       # sorteggia in ordine alfabetico
    print(house)

# Cambiando da lista a set

houses = set()
for student in students:
    if student["house"]not in houses:
        houses.add(student["house"])

for house in sorted(houses):      
    print(house)


# ----------------------------- Global -----------------------------------

balance = 0

def main():
    print("Balance", balance)


if __name__ == "__main__":
    main()

# Aggiungendo 3 funzioni ==== Unbound Local Error 
# E risolvendo errore UnboundLocalError 

balance = 0

def main():
    print("Balance", balance)
    deposit(100)
    withdraw(50)
    print("Balance", balance)

def deposit(n):
    global balance
    balance += n

def withdraw(n):
    global balance
    balance -= n


if __name__ == "__main__":
    main()


# Usando OOP 
# property = Dove una proprietà è una variabile istanza in qualche modo protetta
# Mi permette di controllare che possa essere letta e scritta.
# (getter) // Ma ora posso impedire a codice come il mio in main di cercare di cambiare balance.
# NON avendo definito un setter 
class Account:
    def __init__(self):
        self._balance = 0

    @property
    def balance(self):
        return self._balance

    def deposit(self, n):
        self._balance += n
    
    def withdraw(self, n):
        self._balance -= n

def main():
    account = Account()
    print("Balance", account.balance)
    account.deposit(100)
    account.withdraw(50)
    print("Balance", account.balance)


if __name__ == "__main__":
    main()


# ----------------------- Valori Costanti ---------------------------------

for _ in range(3):
    print("meow")

# valori costanti ("Rendere i valori che non si dovrebbero modificare dando le maiuscole")

MEOWS = 3

for _ in range(MEOWS):
    print("meow")

# Valori che non dovrebbero essere modificati in classi

class Cat:
    MEOWS = 3

    def meow(self):
        for _ in range(Cat.MEOWS):
            print("meow")

cat = Cat()
cat.meow()


# -------------------------- Type Hints ---------------------------------------
# mypy / pip install mypy

def meow(n):
    for _ in range(n):
        print("meow")

number = input("Number: ")
meow(number)
# Errore perche number deve essere int

# Eseguo mypy piu il nome del file in cui sono:

def meow(n: int):
    for _ in range(n):
        print("meow")

number = input("Number: ")
meow(number)

# uso corretto di int = 

def meow(n: int):
    for _ in range(n):
        print("meow")

number : int = input("Number: ")
meow(number)


# Esempi di errori e correzioni su type hints

def meow(n: int):
    for _ in range(n):
        print("meow")

number : int = input("Number: ")
meows: str = meow(number)
print(meows)           # Output : meow meow meow None


# Correzione e evitando quel bug / errore / nel terminale scrivere mypy e file

def meow(n: int) -> None:
    for _ in range(n):
        print("meow")

number : int = int(input("Number: "))
meows: str = meow(number)
print(meows)            

# (n: int) -> str:  significa ce prende un intero e restituisce una stringa

def meow(n: int) -> str:
    return "meow\n" * n

number : int = int(input("Number: "))
meows: str = meow(number)
print(meows, end="")            



# ------------------------- docstrings -----------------------------------------

def meow(n: int) -> str:
    return "meow\n" * n

number : int = int(input("Number: "))
meows: str = meow(number)
print(meows, end="")            

# docstring rileva i 3 """ , serve per documentare il codice 

def meow(n: int) -> str:
    """ 
    Meow n times. 

    : param n: Number of times to meow 
    : type n: int
    : raise TypeError : If n is not an int
    : return: A string of n meowsa, one line
    : rtype: str

    """
    return "meow\n" * n

number : int = int(input("Number: "))
meows: str = meow(number)
print(meows, end="")
