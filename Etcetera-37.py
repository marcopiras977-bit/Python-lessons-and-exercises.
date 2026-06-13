# ------------------- map ----------------------------------------
# map è una funzione built-in che applica una funzione a ogni elemento di un iterabile (come una lista) e restituisce un nuovo iterabile con i risultati.

def main():
    yell("This is CS50")


def yell(phrase):
    print(phrase.upper())


if __name__ == "__main__":
    main()
# Output: THIS IS CS50


# usando lista :

def main():
    yell("This is CS50")

def yell(words):
    uppercased = []
    for word in words:
        uppercased.append(word.upper())
    print(*uppercased)

if __name__ == "__main__":
    main()

# Output: THIS IS CS50


# usando *args:

def main():
    yell("This is CS50")

def yell(*words):   # *words indica che voglio accettare un numero variabile di argomenti posizionali, e che questi saranno raccolti in una tupla chiamata words.
    uppercased = []
    for word in words:
        uppercased.append(word.upper())
    print(*uppercased)

if __name__ == "__main__":
    main()
    
# Output: THIS IS CS50


# Usando Map(): // map(functions, iterable) // la funzione map prende due argomenti: una funzione e un iterabile. Applica la funzione a ogni elemento dell'iterabile e restituisce un nuovo iterabile con i risultati.

def main():
    yell("This is CS50")

def yell(*words):
    uppercased = map(str.upper, words)  # str.upper è una funzione built-in che prende una stringa e restituisce la stessa stringa in maiuscolo. map applica questa funzione a ogni elemento di words, restituendo un iterabile di parole maiuscole.
    print(*uppercased)

if __name__ == "__main__":
    main()
    
# Output: THIS IS CS50

# map è più conciso e leggibile rispetto a un ciclo for, e può essere più efficiente in alcuni casi. Tuttavia, è importante ricordare che map restituisce un iterabile, quindi se si vuole ottenere una lista o una tupla, è necessario convertirlo esplicitamente usando list() o tuple().



# ------------------- List Comprehensions ----------------------------------------
# List comprehensions sono una sintassi concisa per creare liste a partire da iterabili esistenti, applicando una trasformazione o un filtro a ogni elemento.

def main():
    yell("This is CS50")

def yell(*words):
    uppercased = [word.upper() for word in words]  # Questa è una list comprehension che crea una nuova lista uppercased. Per ogni word in words, applica il metodo upper() e aggiunge il risultato alla lista uppercased.
    print(*uppercased)

if __name__ == "__main__":
    main()

# Output: THIS IS CS50



# -------------------- Filter ----------------------------------------
# filter è una funzione built-in che prende una funzione e un iterabile, e restituisce un nuovo iterabile contenente solo gli elementi dell'iterabile originale per cui la funzione restituisce True.
# filter(functions, iterable) // la funzione filter prende due argomenti: una funzione e un iterabile. Applica la funzione a ogni elemento dell'iterabile e restituisce un nuovo iterabile con i risultati.

students = [
    {"name": "Hermione" , "house": "Gryffindor"},
    {"name": "Harry" , "house": "Gryffindor"},
    {"name": "Ron" , "house": "Gryffindor"},
    {"name": "Draco" , "house": "Slytherin"},
    {"name": "Padma" , "house": "Ravenclaw"}
]

gryffindors = [
    student["name"] for student in students if student["house"] == "Gryffindor"
]

for gryffindors in sorted(gryffindors):
    print(gryffindors)
# Output:
# Hermione  
# Harry     
# Ron       

# Filter:

def is_gryffindor(student):
    return student["house"] == "Gryffindor"

gryffindors = filter(is_gryffindor, students) 

for gryffindor in sorted(gryffindors, key=lambda student: student["name"]):  # key lambda student: student["name"] è una funzione anonima che prende un argomento student e restituisce il valore associato alla chiave "name" di quel dizionario. In questo modo, sorted ordina i dizionari in base al nome dello studente.
    print(gryffindor["name"])
# 


# ------------------------ dict comprehension ----------------------------------------
# dict comprehensions sono una sintassi concisa per creare dizionari a partire da iterabili esistenti, applicando una trasformazione o un filtro a ogni elemento.
# sintassi: {key_expression: value_expression for item in iterable if condition}

students = ["Hermione", "Harry", "Ron"]

gryffindors = []

for student in students:
    gryffindors.append({"name": student, "house": "Gryffindor"})

print(gryffindors)
# Output: [{'name': 'Hermione', 'house': 'Gryffindor '}, {'name': 'Harry', 'house': 'Gryffindor'}, {'name': 'Ron', 'house': 'Gryffindor'}]

# dict comprehension:

students = ["Hermione", "Harry", "Ron"]

gryffindors = {student: "Gryffindor" for student in students}  # Questa è una dict comprehension che crea un nuovo dizionario gryffindors. Per ogni student in students, aggiunge una coppia chiave-valore al dizionario, dove la chiave è student e il valore è "Gryffindor". 

print(gryffindors)
# Output: {'Hermione': 'Gryffindor', 'Harry': 'Gryffindor', 'Ron': 'Gryffindor'}



# ------------------------- enumerate ----------------------------------------

students = ["Hermione", "Harry", "Ron"]

for i in range(len(students)):
    print(i, students[i])

# Output:
# 0 Hermione
# 1 Harry
# 2 Ron

students = ["Hermione", "Harry", "Ron"]

for i in range(len(students)):
    print(i + 1, students[i])

# Output: 
# 1 Hermione
# 2 Harry
# 3 Ron

students = ["Hermione", "Harry", "Ron"]

for i, student in enumerate(students):
    print(i + 1, student)

# Output:
# 1 Hermione
# 2 Harry
# 3 Ron



# ------------------------- generators ----------------------------------------
# I generatori sono un tipo speciale di iteratore che consente di generare valori su richiesta, invece di memorizzarli tutti in memoria. Sono utili quando si lavora con grandi quantità di dati o quando si desidera creare sequenze infinite.

n = int(input("What's n?"))
for i in range(n):
    print(i)
# Output: se n è 5, stampa 0, 1, 2, 3, 4


def main():
    n = int(input("What's n?"))
    for i in range(n):
        print(i)

if __name__ == "__main__":
    main()

# Output: se n è 5, stampa 0, 1, 2, 3, 4


def main():
    n = int(input("What's n?"))
    for i in range(n):
        print(sheep(i))

def sheep(n):
    return f"{n} sheep"

if __name__ == "__main__":
    main()
# Output: se n è 3, stampa:
# 0 sheep
# 1 sheep
# 2 sheep


# Generatori:

def main():
    n = int(input("What's n?"))
    for s in sheep(n):
        print(s)

def sheep(n):
    flock = []
    for i in range(n):
        flock.append(f"{i} sheep")
    return flock

if __name__ == "__main__":
    main()
# non funziona sopra i 1 milione di pecore, perché la lista flock occupa troppa memoria.


# yield è una parola chiave che consente di creare un generatore. Quando una funzione contiene yield, diventa un generatore e restituisce un iteratore che produce valori uno alla volta, ogni volta che viene chiamato next().

def main():
    n = int(input("What's n?"))
    for s in sheep(n):
        print(s)

def sheep(n):
    for i in range(n):
        yield f"{i} sheep"

if __name__ == "__main__":
    main()

# 