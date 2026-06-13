
# Leggere i dati 

with open("temperature.txt", "r") as f:
    righe = f.readlines()

# analizzare 

allarmi = 0

for riga in righe:
    valore = int(riga.strip())
    if valore > 80:
        allarmi += 1

# scrivere risultato 

with open("report.txt", "w") as f:
    f.write(f"Numero allarmi: {allarmi}")



# Esempio concreto:

Numero_allarmi = 0
totale_letture = 0
macchine_off = 0

with open("log_macchine.txt", "r") as f:
    righe = f.readlines()

    for riga in righe:
        totale_letture += 1

        parti = riga.strip().split(",")

        macchina = parti[0]
        temperatura = int(parti[1])
        stato = parti[2]

        if temperatura > 80:
            Numero_allarmi += 1

        if stato == "OFF":
            macchine_off += 1


with open("report.txt", "w") as f:
    f.write(f"Totale letture: {totale_letture}\n")
    f.write(f"Numero allarmi: {Numero_allarmi}\n")
    f.write(f"Macchine OFF: {macchine_off}\n")


# Piu completo e reale: 

# nizializzo contatori
totale_letture = 0
allarmi = 0
macchine_off = 0

try:
    # Leggo il file
    with open("log_macchine.txt", "r") as f:
        righe = f.readlines()

    # Elaboro i dati
    for riga in righe:
        try:
            parti = riga.strip().split(",")
            macchina = parti[0]
            temperatura = int(parti[1])
            stato = parti[2]

            totale_letture += 1

            if temperatura > 80:
                allarmi += 1

            if stato.upper() == "OFF":
                macchine_off += 1

        except ValueError:
            print(f"Errore di conversione in riga: {riga.strip()}")

except FileNotFoundError:
    print("Il file log_macchine.txt non esiste!")

# Scrivo il report in un nuovo file
try:
    with open("report.txt", "w") as f:
        f.write(f"Totale letture: {totale_letture}\n")
        f.write(f"Numero allarmi: {allarmi}\n")
        f.write(f"Macchine OFF: {macchine_off}\n")
except IOError:
    print("Errore scrittura file report.txt")