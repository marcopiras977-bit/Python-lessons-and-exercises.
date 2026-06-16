# PYTHON DEVELOPER PROGRAM 1

#print( 235 < 1)    #False            # comparare numeri 
#print( 101 > 90)   #True
#print( 11 >= 11)   #True 

#print( "online" == "online")         # comparare stringhe (" ")
#print( "online" != "offline")
fruit_1 = "apple"
fruit_2 = "oranges"
#print( fruit_1 == fruit_2)   /  # False

is_ready = True
fuel_deposit = 59.89
best_grade = "A"
number_of_pets = 2
print(type(is_ready))           # class boolean (bool)
print(type(fuel_deposit))       # class float
print(type(best_grade))         # class str
print(type(number_of_pets))     # class int

eta_Karla = 29
eta_cp = 1
diff = eta_Karla - eta_cp
print(f' Karla hai {diff} anni piu di me!!')

age = 28 
name_and_age = "Marco : {}".format(age)      # .format() inserisce un dato ... // {} questo dice "aspetto un valore" , se ce ne fossero di piu ( {},{},...) significa che aspetta piu variabili

print(name_and_age)                           # es: "Marco : {} {} {}" .format (age, height, altro )

# + - / * % // ** --- not or and --- 



############### STRING SLICING ###########################################################

def main():
    phone = "617-495-1000"
    print(phone[0:3]) # Output solo 617 i primi 3 numeri
    print(phone[:3]) # Output solo e sempre 617 
    print(phone[8:12]) # Output solo ultii 4 numeri "1000"
    print(phone[8:]) # Output dal ottavo fino in fondo
    print(phone[-4:]) # Output parte dalla fin e"-1"

main()
