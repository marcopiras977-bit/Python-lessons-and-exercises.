class dog:
    latin = "canis"

    def __init__(self, colour = "brown"):
        self.colour = colour
        self.latin += colour

first=dog()
second=dog("red")
third=dog("white")
print(third.latin)


def get_guess():
    guess = int(input("Enter a guess: "))
    return guess

def main():
    guess = get_guess()
    if guess == 50:
        print("Correct")
    else:
        print("Incorrect")

main()

# returns serve a indicare il valore di una funzione
# return interrompe l'esecuzione della funzione
def add(a, b):
    return a + b
result = add(3, 5)
print(result)

# return può essere usato anche senza valore per terminare una funzione
def check_even(num):
    if num % 2 == 0:
        return True
    return False