######## EXCEPTIONS #######

#print("Hello)   #syntax Error: missing closing quotation mark
#print(10 / 0)  # ZeroDivisionError: division by zero
#print(int("abc"))  # ValueError: invalid literal for int() with base 10 -> 


# try, except , finally, block, else 
# try:
    # esegue il codice che potrebbe generare errore
# except 
    # cosa fare se c'è un errore
# else:
    # cosa fare se NON c'è stato nessun errore
# finally: 
    # cosa fare SEMPRE,anche con errori / non viene mai saltato / Si USA spesso in close() di file, chiusura connessioni, rilascio risorse

# try: "Provo"
# except "Se sbaglio"
# else: "Se va tutto bene"
# finally: "In ogni caso"


# ATTENZIONE: Break si usa in try MA SOLO SE il try è dentro un ciclo for o while


#-------------------------------------------------------------------------
#ValueError
x = int(input("What s is x?"))
print(f"x is {x}")
 
try:
    x = int(input("What s is x?"))
    print(f"x is {x}")

except ValueError:
    print("That is not a valid number. Please try again.")

#-------------------------------------------------------------------------
# Due linee di codice error handling
# NameError/ "Eccezione"

try:
    x = int(input("What s is x?"))
except ValueError:
    print("That is not a integer")

print(f"x is {x}") # se scrivo "gatto" esempio , mi da comunque l'errore perche x non è definito

#-------------------------------------------------------------------------
# else
# "se tutto va bene ""esegui""
try:
    x = int(input("What s is x?"))
except ValueError:
    print("That is not a integer")
else:
    print(f"x is {x}") # Aggiungendo else: bypassa la condizione nel caso x non è integer o definito

#--------------------------------------------------------------------------
# Migliorando il codice e chiedendo l'input finche l'utente non scrive giusto

while True:
    try:
        x = int(input("What s is x?"))
    except ValueError:
        print("That is not a integer")
    else:
        print(f"x is {x}")

#-----------------------------------------------------------------------
# Altro scenario,con break per uscire dal ciclo quando l'input è corretto

while False:
    try:
        x = int(input("What s is x?"))
    except ValueError:
        print("That is not a integer")
    else:
        break

print(f"x is {x}")

#-----------------------------------------------------------------------
# Funzione per gestire l'input e errori

def main():
    x = get_int()
    print(f'x is {x}')

def get_int():
    while True:
        try:
            x = int(input("What s is x?"))
        except ValueError:
            print("That is not a integer")
        else:
            return x
    
main()

#-----------------------------------------------------------------------
# pass statement / ignorare l'errore 

def main():
    x = get_int()
    print(f'x is {x}')

def get_int():
    while True:
        try:
            return int(input("What s is x?"))
        except ValueError:
            pass

main()
#-----------------------------------------------------------------------

def main():
    x = get_int()
    print(f'x is {x}')

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass

main()
#-----------------------------------------------------------------------
# raise statement / generare eccezioni personalizzate

def main():
    x = get_int("What s is x?")
    print(f'x is {x}')

def get_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                raise ValueError("Negative value not allowed.")
            return value
        except ValueError as e:
            print(e)    
main()
#-----------------------------------------------------------------------

# Riassunto:
# - Per gestire le eccezioni, basta usare il costrutto try/except e gestire le eccezioni specifiche che si vogliono gestire.
# - Per sollevare un'eccezione, basta usare la parola chiave raise seguita dal tipo di eccezione che si vuole sollevare e un messaggio opzionale.   
