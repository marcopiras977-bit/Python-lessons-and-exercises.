# (modificando il file students.csv)

# Questo codice utilizza il modulo csv per leggere i dati dal file students.csv. La funzione csv.reader() legge il file e restituisce un iteratore che produce ogni riga del file come una lista di valori. Nel ciclo for, ogni riga viene memorizzata come un dizionario con le chiavi "name" e "home", e questi dizionari vengono aggiunti alla lista students. Infine, la lista students viene ordinata in base al nome dello studente utilizzando una funzione lambda come chiave di ordinamento, e i risultati vengono stampati a schermo. 


# csv.DictReader() è una classe del modulo csv che legge un file CSV e restituisce ogni riga come un dizionario, dove le chiavi sono i nomi delle colonne e i valori sono i dati corrispondenti a quelle colonne. In questo modo, puoi accedere ai dati in modo più intuitivo utilizzando i nomi delle colonne invece di dover ricordare l'indice di ogni campo. Ad esempio, se il tuo file CSV ha una colonna "name" e una colonna "home", puoi accedere a questi valori come student["name"] e student["home"] invece di dover usare student[0] e student[1].

import csv

students = []

with open("students.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            students.append({"name": row["name"], "home": row["home"]})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")


# (Modificando il file "students.csv" aggiungendo altri dati)
# funziona lo stesso anche se invece di due colonne, ci sono/ saranno piu colonne, basta che i nomi delle colonne siano corretti e corrispondano a quelli utilizzati nel codice. 
import csv

students = []

with open("students.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            students.append({"name": row["name"], "home": row["home"]})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")



# (modificando il file "students.csv")
# scrive una nuova riga nel file CSV con i valori name e home, separati da una virgola. La funzione writerow() accetta una lista di valori e li scrive come una riga nel file CSV, con i valori separati da virgole. In questo caso, stiamo scrivendo il nome e la casa dello studente come una nuova riga nel file CSV.

import csv 

name = input("What's your name? ")
home = input("Where do you live? ")

with open("students.csv", "a") as file:
    writer  = csv.writer(file)
    writer.writerow([name, home])



# csv.DictWriter() è una classe del modulo csv che consente di scrivere dati in un file CSV utilizzando un dizionario. Quando si utilizza csv.DictWriter(), è necessario specificare i nomi delle colonne (fieldnames) che si desidera utilizzare nel file CSV. La funzione writerow() accetta un dizionario come argomento, dove le chiavi corrispondono ai nomi delle colonne e i valori corrispondono ai dati da scrivere in quelle colonne. In questo modo, puoi scrivere i dati in modo più intuitivo utilizzando i nomi delle colonne invece di dover ricordare l'ordine dei campi. Ad esempio, se il tuo file CSV ha una colonna "name" e una colonna "home", puoi scrivere i dati come {"name": name, "home": home} invece di dover usare [name, home].

import csv 

name = input("What's your name? ")
home = input("Where do you live? ")

with open("students.csv", "a") as file:
    writer  = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})

