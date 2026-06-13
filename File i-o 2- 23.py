# Sul file students.csv:
# CSV file: è un formato di file che utilizza una virgola per separare i valori. Ogni riga del file rappresenta un record e ogni campo all'interno del record è separato da una virgola. Ad esempio, un file CSV potrebbe contenere dati come questo:

# Hermione,Gryffindor
# Harry,Gryffindor
# Ron,Gryffindor
# Draco,Slytherin

# Adesso su un file students.py:

# rstrip() rimuove eventuali spazi bianchi o caratteri di nuova linea alla fine della stringg
# print(f"{name} is in {house}") # name è il nome dello studente e house è la casa a cui appartiene



# Creare una lista di dizionari per memorizzare i dati degli studenti:

students  =[]

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students.append({"name": name, "house": house}) # aggiunge un dizionario con le chiavi "name" e "house" alla lista students

for student in sorted(students):
    print(student)


# sorting by student name:

students  =[]

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house} # crea un dizionario con le chiavi "name" e "house" e i valori corrispondenti
        students.append(student)

for student in sorted(students):
    print(f"{student['name']} is in {student['house']}") # student['name'] accede al valore associato alla chiave "name" nel dizionario student, e student['house'] accede al valore associato alla chiave "house" nel dizionario student


# Dire a python di ordinare gli studenti in base al nome invece che all'intero dizionario:

students  =[]

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house} 
        students.append(student)

def get_name(student):
    return student["name"]

# passando get_name alla funzione sorted(), stiamo dicendo a Python di utilizzare il valore restituito da get_name(student) come chiave per ordinare gli studenti. In questo caso, get_name(student) restituisce il nome dello studente, quindi gli studenti verranno ordinati in base al loro nome.
for student in sorted(students, key=get_name, reverse = True): # reverse=True ordina in ordine inverso
    print(f"{student['name']} is in {student['house']}")



# Funzione Lambda: 
# sintassi lambda arg1, arg2, ... : expression
# La funzione lambda è una funzione anonima, ovvero una funzione senza un nome. Viene spesso utilizzata quando si ha bisogno di una funzione semplice e veloce da definire, senza dover creare una funzione completa con un nome. Ad esempio, se vogliamo ordinare gli studenti in base al nome senza dover definire una funzione separata, possiamo utilizzare una funzione lambda direttamente all'interno della chiamata a sorted(): 

students  =[]

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house} 
        students.append(student)

# lambda student: student["name"] è una funzione anonima che prende un argomento student e restituisce il valore associato alla chiave "name" nel dizionario student. In questo modo, sorted() utilizza il nome dello studente come chiave per ordinare gli studenti.
for student in sorted(students, key=lambda student: student["name"]): 
    print(f"{student['name']} is in {student['house']}")
