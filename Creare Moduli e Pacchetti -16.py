# Creating Modules and Packages

import requests

def main():
    artwork = input("Artwork: ")
    artworks = get_artworks(query=artwork, limit=3)
    for artwork in artworks:
        print(f"* {artwork}")

def get_artworks(query,limit):
    try: 
        response = requests.get("https://api.artic.edu/api/v1/artworks/search", {"q": query,"limit": limit})
        response.raise_for_status()
    except requests.HTTPError:
        return []
    
    content = response.json()
    return [artwork["title"] for artwork in content["data"]]

if __name__ == "__main__":
    main()

# questo codice è un esempio di come creare un modulo e importarlo in un altro file, in questo caso abbiamo creato una funzione get_artworks che fa una richiesta a un'
# serve API per cercare opere d'arte e restituire i titoli delle opere trovate, poi abbiamo importato questa funzione in un altro file e l'abbiamo usata per cercare opere d'arte e stampare i titoli.
# Per creare un modulo, basta creare un file con estensione .py e definire le funzioni o le classi che si vogliono includere nel modulo, poi per importare il modulo in un altro file, basta usare la parola chiave import seguita dal nome del modulo.
# Per creare un pacchetto, basta creare una cartella con un file __init__.py al suo interno, poi si possono creare altri file .py all'interno della cartella per definire le funzioni o le classi che si vogliono includere nel pacchetto, poi per importare il pacchetto in un altro file, basta usare la parola chiave import seguita dal nome del pacchetto.

# Riassunto:
# - Un modulo è un file che contiene definizioni di funzioni, classi e variabili che possono essere importate in altri file.
# - Un pacchetto è una cartella che contiene un file __init__.py e altri file .py che definiscono funzioni, classi e variabili che possono essere importate in altri file.  
# - Per creare un modulo, basta creare un file con estensione .py e definire le funzioni o le classi che si vogliono includere nel modulo.
# - Per importare un modulo in un altro file, basta usare la parola chiave import seguita dal nome del modulo.
# - Per creare un pacchetto, basta creare una cartella con un file __init__.py al suo interno, poi si possono creare altri file .py all'interno della cartella per definire le funzioni o le classi che si vogliono includere nel pacchetto.        

