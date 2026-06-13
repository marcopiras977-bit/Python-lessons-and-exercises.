# liste e dizionari comprehensions
# da fare questo codice se devo prendere da un testo un determinato numero di parole e inserirle in un dizionario ,con condizioni
def main():

    words = "A" #get_words("addres.txt") 
    lowercase_words = [word.lower() for word in words if len(word) > 4] 
    # per ogni word nella lista words prendi word,includendo solo la lunghezza di 4
    # list comprehension

    counts = {}

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    # questo sopra trasformato in dictionary comprehension
    counts = {word: words.count(word) for word in lowercase_words}
    # """Per ogni parola in questa lista di parole minuscole,Assegna una key,imposta il valore sul count/conteggio
    #    per ogni volta che compare word """
    ##save_counts(counts)

main()

