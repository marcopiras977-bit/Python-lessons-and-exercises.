# Collezioni : Tuple 

# Tuple --- variabili/liste non modificabili

high_score = ("Marco", 120)
print(high_score)

high_score = ("Holly",150)
print(high_score)

# high_score [0] = " abcdf" # non si puo riassegnare un lista 

# si puo cercare / trovare il numero piu alto nella lista di High_score : in questo caso uscirà Holly perche ha il numero piu alto
name = high_score[0]
print(name)

# si puo trovare la lunghezza del tuple 
print(len(high_score))# uscira 2 , perche ce Marco e Holly

# IN operatore --- verificare se un oggetto è presente nella tupla 
print("Marco" in high_score)  # False perche "Marco NON è nel punteggio piu alto (high_score)
print("Holly" in high_score)  # True perche "Marco è nel punteggio piu alto (high_score)

# Recap 
print(name[0])     # perche : name = high_score -> "holly" PERò [0] qundi solo la prima lettera
print(name[0:2])   # perche : name = high_score -> "holly" PERò [0:2] quidi solo le prime due lettere
print("Hol"in name) # perche : è Vero che è presente Hol in "Holly"
print(len(name))   # perche : len() la lunghezza di name è 5 lettere




################################### Tuples #####################################

# PER SAPERE LA MEMORIA USATA si usa import sys e .getsizeof()
import sys

def main():
    latitude = 42.376
    longitude= -71.115

    # variabili salvati in una tuple
    coordinates = (42.376,-71.115 )
    print(f'Latitude: {coordinates[0]}')
    print(f'Latitude: {coordinates[1]}')

    coordinate_tuple = (42.376,-71.115)
    coordinate_list = [42.376,-71.115]
    print(f"{sys.getsizeof(coordinate_tuple)} bytes") # usano meno Memoria
    print(f"{sys.getsizeof(coordinate_list)} bytes") # Usa piu Memoria
    # Tupla: immutabile

main()
