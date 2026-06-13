# Reading and writing CSV files: shorts 

# ce un file chiamato : "views.csv" con 3 colonne di dati 1. id, 2. titolo, 3. autore.

# si crea un file : views.py 
import csv
import numpy as np
from PIL import Image

def main():
    with open("views.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row)

def calculate_brightness(filename):
    with Image.open(filename) as img:
        brightness = np.mean(np.array(img.convert("L"))) / 255 
    return brightness 

main()

# Output: saranno stampate tutte le righe del file "views.csv" come dizionari, con le chiavi corrispondenti ai nomi delle colonne (id, titolo, autore).


# -----------------------------------------------------------------------------

# questo codice legge il file "views.csv", calcola la luminosità di ogni immagine corrispondente agli id presenti nel file e stampa i valori di luminosità.

import csv
import numpy as np
from PIL import Image

def main():
    with open("views.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            brightness = calculate_brightness(f"{row['id']}.jpeg")
            print(brightness)

def calculate_brightness(filename):
    with Image.open(filename) as img:
        brightness = np.mean(np.array(img.convert("L"))) / 255 
    return brightness 

main()

# Output: saranno stampati i valori di luminosità per ogni immagine corrispondente agli id presenti nel file "views.csv". Ogni immagine deve essere salvata con il nome "id.jpeg" nella stessa directory del file "views.csv".


#-----------------------------------------------------------------------------


# Questo codice serve per leggere il file "views.csv", calcolare la luminosità di ogni immagine corrispondente agli id presenti nel file e scrivere i risultati in un nuovo file chiamato "analysys.csv" con una nuova colonna chiamata "brightness".

import csv
import numpy as np
from PIL import Image

def main():
    with open("views.csv", "r") as views, open("analysys.csv", "w") as analysis:
        reader = csv.DictReader(views)
        writer = csv.DictWriter(analysis, fieldnames= reader.fieldnames + ["brightness"]) # serve per aggiungere una nuova colonna al file "analysys.csv" chiamata "brightness"
        writer.writeheader()
        
        for row in reader:
            brightness = calculate_brightness(f"{row['id']}.jpeg")
            writer.writerow(
                {
                    "id":row["id"],
                    "titolo":row["titolo"],
                    "autore":row["autore"],
                    "brightness":brightness
                }
            )

def calculate_brightness(filename):
    with Image.open(filename) as img:
        brightness = np.mean(np.array(img.convert("L"))) / 255 
    return brightness 

main()

# Output: saranno scritti i dati del file "views.csv" insieme ai valori di luminosità calcolati per ogni immagine corrispondente agli id presenti nel file "views.csv" in un nuovo file chiamato "analysys.csv". Il nuovo file conterrà le stesse colonne del file "views.csv" più una nuova colonna chiamata "brightness" con i valori di luminosità corrispondenti a ogni immagine.

# -----------------------------------------------------------------------------


# codice più compatto per leggere il file "views.csv", calcolare la luminosità di ogni immagine corrispondente agli id presenti nel file e scrivere i risultati in un nuovo file chiamato "analysys.csv" con una nuova colonna chiamata "brightness". 


import csv
import numpy as np
from PIL import Image

def main():
    with open("views.csv", "r") as views, open("analysys.csv", "w") as analysis:
        reader = csv.DictReader(views)
        writer = csv.DictWriter(analysis, fieldnames= reader.fieldnames + ["brightness"]) # serve per aggiungere una nuova colonna al file "analysys.csv" chiamata "brightness"
        writer.writeheader()
        
        for row in reader:
            row["brightness"] = round(calculate_brightness(f"{row['id']}.jpeg")) # serve per aggiungere una nuova key al dizionario "row" chiamata "brightness" con il valore di luminosità calcolato per ogni immagine corrispondente agli id presenti nel file "views.csv". La funzione round() serve per arrotondare il valore di luminosità a un numero intero.
            writer.writerow(row)


def calculate_brightness(filename):
    with Image.open(filename) as img:
        brightness = np.mean(np.array(img.convert("L"))) / 255 
    return brightness 

main()