from math import sqrt

hello_message = """
Benvenuti al programma calcolatrice:
Funzioni disponibili:

- Addizioni = 1
- Sottrazione = 2
- Moltiplicazioni = 3
- Divisione = 4
- Calcolo Esponenziale = 5
- Radice Quadrata = 6
- Uscire = ESC
"""

while True:
    print(hello_message)

    action = input("Inserisci un numero: ")

    if action == "1":
        print("\nAddizione\n")
        a = float(input("Inserisci un numero: "))
        b = float(input("inserisci secondo numero: "))
        print("risultato è: ", str(a + b))

    elif action == "2":
        print("\nSottrazione\n")
        a = float(input("Inserisci un numero: "))
        b = float(input("inserisci secondo numero: "))
        print("risultato è: ", str(a - b))

    elif action == "3":
        print("\nMoltiplicazione\n")
        a = float(input("Inserisci un numero: "))
        b = float(input("inserisci secondo numero: "))
        print("risultato è: ", str(a * b))

    elif action == "4":
        print("\nDivisione\n")
        a = float(input("Inserisci un numero: "))
        b = float(input("inserisci secondo numero: "))
        print("risultato è: ", str(a / b))

    elif action == "5":
        print("\nCalcolo Esponenziale\n")
        a = float(input("Inserisci un numero: "))
        b = float(input("inserisci secondo numero: "))
        print("risultato è: ", str(a ** b))

    elif action == "6":
        print("\nRadice Quadrata\n")
        a = float(input("Inserisci un numero: "))
        print("risultato è: ", str(sqrt(a)))

    elif action == "ESC":
        print("\nApplicazione in chiusura\n")

    new_action = input("\nContinui? S/N ")
    if new_action == "N" or new_action ==  "n":
        print("A presto!\n")
        break
