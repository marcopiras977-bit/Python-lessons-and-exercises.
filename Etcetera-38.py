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

#  Fine di introduzione a programmare in Python. CS50 , David J. Malan, Harvard University, 2026.


# Ultimo programma: say.py

"""
 import cowsay
 import pyttsx3

 engine = pyttsx3.init()
 this =  input("What should I say? ")
 cowsay.say(this)
 engine.say(this)
 engine.runAndWait()
 """

# output: se l'input è "This was CS50", stampa una mucca che dice "This was CS50" e pronuncia "This was CS50" ad alta voce.



# -------------- recursion / etcetera short -------------------------
# La ricorsione è una tecnica di programmazione in cui una funzione chiama se stessa per risolvere un problema. È spesso utilizzata per risolvere problemi che possono essere suddivisi in sottoproblemi più piccoli, come il calcolo di fattoriali, la ricerca in alberi o la generazione di sequenze.

# 3! = 3*2*1 == 3! = 3*2!
# 2! = 2*1 == 2! = 2*1!

def factorial(n):
    if n == 1:
        return 1
    
    return n * factorial(n-1)  # 2 perche fsctorial(3) quindi 3 - 1


result = factorial(3)

# output 6