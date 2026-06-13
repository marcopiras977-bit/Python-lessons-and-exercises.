# Shorts Regular Expressions

# colori esadecimali (#000000 = nero / #FFFFFF = Bianoc ecc...)

# match funziona solo search trova il pattern che cerco nell'input code
# match.group() farà vedere esattamente cosa search ha trovatcome corrispondenza per il pattern

import re

def main():
    code = input("Hexadecimal color code: ")

    pattern = r"^#[a-fA-F0-9]{6}$"
    match = re.search(pattern, code)
    if match:
        print(f"Valid. Matched with {match.group()}")
    else:
        print("Invalid.")
main()


# Short Capture Groups


import re

locations = {"+1": "United Sttes and Canada", "+62": "Indonesia", "+505": "Nicaragua"}

def main():

    pattern = r"\+\d{1,3} \d{3}-\d{3}-\d{4}"
    number = input("Number: ")

    match = re.searc(pattern, number)
    if match:
        print("Valid")
    else:
        print("Invalid")

main()


# per trovare da dove è il numero chiamante :
# estrarre il prefisso 

import re

locations = {"+1": "United Sttes and Canada", "+62": "Indonesia", "+505": "Nicaragua"}

def main():

    pattern = r"(?P<country_code>\+\d{1,3}) \d{3}-\d{3}-\d{4}"  # in parentesi c'è il primo gruppo
    number = input("Number: ")

    match = re.search(pattern, number)
    if match:
        country_code = match.group("country_code")
        print(locations[country_code])
    else:
        print("Invalid")

main()


