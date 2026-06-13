# api calls 
# documentazione API calls :
# richiesta ad un sito di certe informazioni con risposta
import requests

def main():
    response = requests.get("https://api.artic.edu/api/v1/artworks/search")
    print(response)          # Output [200], significa richiesta andata a buon fine

# richiesta dati dal sito,sottoforma di Json [una collezione di keys and values]
    content = response.json()
    print(content)

# ricavare e cercare il JSON
    for artwork in content["data"]:
        print(f" {artwork['title']}")


main()

# Handling errors di connessione / rete

def main():
    try:
        response = requests.get("https://api.artic.edu/api/v1/artworks/search")
        response.raise_for_status()  # Controlla se la risposta ha funzionato
    except requests.HTTPError:       # Se non è stato possibile stampa il messaggio
        print("Non è stato possibile fare richiesta")
        return
    content = response.json()
    for artwork in content["data"]:
        print(f" {artwork['title']}")

main()


# Introducendo Parametri (tramite documentazione) per rendere API piu potente
# es: "q" cerca un query 
# Chiedendo al utente di trovare un specifico artista nel sito di Arte di Chicago

# import requests

def main():
    print("Search the Art Institute of Chicago!")
    artist = input("Artist: ")
    try:
        response = requests.get(
            "https://api.artic.edu/api/v1/artworks/search",
            {"q": artist})
        response.raise_for_status()  
    except requests.HTTPError:       
        print("Non è stato possibile fare richiesta")
        return
    content = response.json()
    for artwork in content["data"]:
        print(f" {artwork['title']}")

main()


# Riassunto:
# - Per fare una richiesta API, basta usare la funzione requests.get() e passare l'URL del sito a cui si vuole fare la richiesta.
# - Per controllare se la richiesta è andata a buon fine, basta usare il metodo raise_for_status() e gestire l'eccezione HTTPError se la richiesta non è andata a buon fine.
# - Per ottenere i dati dalla risposta, basta usare il metodo json() e accedere ai dati usando le chiavi del JSON.  
