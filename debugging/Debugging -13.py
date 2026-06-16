# DEBUGGING -13

def main():
    height = int(input("Height: "))
    pyramid(height)

def pyramid(n):
    for i in range(n):
        print("#" * i)

if __name__ == "__main__":
    main()


# <--- breakpoint
# serve a fermare l'esecuzione del programma in un punto specifico per esaminare lo stato delle variabili e il flusso di esecuzione.
# tasto play con uninsetto che sembra una coccinella

# Handling exceptions

distances = { "voyager 1": "163",
             "voyager 2": "136",
             "Pioneer 10": "80",
             "New Horizons": "58",
             "Pioneer 11": "44"}

def main():
    spacecraft = input("Enter a specacraft: ")
    m = convert(distances[spacecraft])
    print(f'{m} m away')

def convert(au):
    return au * 149597870700

main()

#---------- Errori da valutare con try except finally else ---------------

distances = { "voyager 1": "163",
             "voyager 2": "136",
             "Pioneer 10": "80 AU",
             "New Horizons": "58",
             "Pioneer 11": "44 AU"}

def main():
    spacecraft = input("Enter a specacraft: ")
    au = float(distances[spacecraft])  # convertire le str in numeri float di un dizionario
    m = convert(au)
    print(f'{m} m away')

def convert(au):
    return au * 149597870700

main()

# altri conversioni e errori di scrittura nel dizionario

distances = { "voyager 1": "163",
             "voyager 2": "136",
             "Pioneer 10": "80 AU",
             "New Horizons": "58",
             "Pioneer 11": "44 AU"}

def main():
    spacecraft = input("Enter a specacraft: ")

    try:                                   # inserendo try e except in caso di non conversione
        au = float(distances[spacecraft])
    except ValueError:
        print(f"Can't convert {distances[spacecraft]} to a float")
        return
    
    m = convert(au)
    print(f'{m} m away')

def convert(au):
    return au * 149597870700

main() 


# Piu errori e eccezioni-----------------------------------------
# se all' input inserisco un nome non nel dizionario ottengo un altro errore:
distances = { "voyager 1": "163",
             "voyager 2": "136",
             "Pioneer 10": "80 AU",
             "New Horizons": "58",
             "Pioneer 11": "44 AU"}

def main():
    spacecraft = input("Enter a specacraft: ")

    try:                                   
        au = float(distances[spacecraft])
    except KeyError:                        # Inserendo un errore eccezione che impedisce i blocco programma
        print(f" {spacecraft} is not in dictionary")
        return
    except ValueError:
        print(f"Can't convert {distances[spacecraft]} to a float")
        return
    
    m = convert(au)
    print(f'{m} m away')

def convert(au):
    return au * 149597870700

main() 

#------------------------------------------------------------------------------
# RAISING ERRORS
# 
# p.s. pace = ritmo 
def main():
    pace = get_pace(miles = 26.2, minutes = 180)
    print(f"you need to run each mile in {round(pace, 2)} minutes.")

def get_pace(miles,minutes):
    return minutes / miles

main()

# Raise = sollevare un exception eccezione

def main():
    pace = get_pace(miles = 26.2, minutes = 0)
    print(f"you need to run each mile in {round(pace, 2)} minutes.")

def get_pace(miles,minutes):
    if not minutes > 0:
        raise Exception()

    return minutes / miles

main()

# Raise eeccezione di ValueError  

def main():
    pace = get_pace(miles = 26.2, minutes = 0)
    print(f"you need to run each mile in {round(pace, 2)} minutes.")

def get_pace(miles,minutes):
    if not minutes > 0:
        raise ValueError()

    return minutes / miles

main()

# Raise eeccezione di ValueError con (messaggio incluso)

def main():
    pace = get_pace(miles = 26.2, minutes = 0)
    print(f"you need to run each mile in {round(pace, 2)} minutes.")

def get_pace(miles,minutes):
    if not minutes > 0:
        raise ValueError("Invalid value for minutes.")

    return minutes / miles

main()


# Riassunto:
# - Per gestire le eccezioni, basta usare il costrutto try/except e gestire le eccezioni specifiche che si vogliono gestire.
# - Per sollevare un'eccezione, basta usare la parola chiave raise seguita dal tipo di eccezione che si vuole sollevare e un messaggio opzionale.   
