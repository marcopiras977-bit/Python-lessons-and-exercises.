# File i/o 

# creo un file names.py e names.txt

names = []

for _ in range(3):
    names.append(input("Enter a name: "))

for name in sorted(names):
    print(f"hello, {name}")


# per salvare i nomi che inserisci in un file.

name = input("What is your name? ")

file = open("names.txt", "a") # "a" sta per "append", che significa che i nuovi dati verranno aggiunti alla fine del file esistente invece di sovrascriverlo
file.write(f"{name}\n") # scrive il nome nel file seguito da un carattere di nuova linea per separare i nomi
file.close() # chiude il file, è importante chiudere i file dopo averli usati per liberare risorse



# with permette di aprire un file e assicura che venga chiuso correttamente anche se si verifica un errore durante l'operazione di scrittura

name = input("What's your name? ")

with open("names.txt", "a") as file: # apre il file in modalità append e lo assegna alla variabile file
    file.write(f"{name}\n") # scrive il nome nel file seguito da un carattere di nuova linea



# Per leggere i nomi dal file e stamparli a schermo:

with open("names.txt", "r") as file: # apre il file in modalità lettura e lo assegna alla variabile file
    lines = file.readlines() # legge tutte le righe del file e le memorizza in una lista chiamata names

for line in lines:
    print(f"hello, {line.rstrip()}") # .strip() rimuove eventuali spazi bianchi o caratteri di nuova linea alla fine della stringa, in questo modo i nomi vengono stampati senza spazi extra o linee vuote


# Forma piu compatta per leggere i nomi dal file e stamparli a schermo:

with open("names.txt", "r") as file:
    for line in file:
        print(f"hello, {line.rstrip()}")  



# Combinare tutte le operazioni in un unico programma:

names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"hello, {name}")


# Reverse alfabetico ordine
# per ordinare in ordine alfabetico inverso, puoi utilizzare il parametro reverse=True nella funzione sorted().
# sorted(iterable, /, *, key=None, reverse=False) 
sorted_names = sorted(names, reverse=True)
for name in sorted_names:
    print(f"hello, {name}") 
