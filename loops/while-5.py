# While loop function

# while condition == True:
    # execute the code mltiple times

position = 0 
end_position = 5

while position < end_position:   # Finche position è inferiore a end_position, ripete incrementando la posizione Finchè arriva alla condizione di True
    position += 1                # Condizione di incremento 
    print(position)

print("you have reached the end")

# break 
# Funzione Break ( per interrompere while)

position = 0 
enemy_position = 10
end_position = 5

while position < end_position:   # Finche position è inferiore a end_position, ripete incrementando la posizione Finchè arriva alla condizione di True
    position += 1                # Condizione di incremento 
    print(position)
    if position == enemy_position:
        print("Game Over")
        break
if position == enemy_position:
    print("you have reached the end")
elif position != enemy_position:
    print("you have avoided the enemy")
else: 
    print("error")
# FINE 

# indovina il numero

guess = 10

while True:
    guess_number = int(input("Guess a number: "))

    if guess_number == guess:
        print("its right!")
        break
    else:
        print("That's not right")


