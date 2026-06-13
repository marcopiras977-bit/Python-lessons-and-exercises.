# Reading & Writing File-27.py

# In un file : "Alice.txt", ce presente un testo 


def main():
    with open("alice.txt", "r") as f:
        contents = f.read()          # fino qua solo leggero il contenuto
        contents = f.readlines()
        print(contents)

    chapter1 = contents[52:272]      # legge solo la parte interessata del testo
    print(chapter1[0])
    with open("chapter1.txt", "w") as f:  # Aprire un nuovo file di nome chapter1.txt
        f.write("Chapter I.")             # e ci scrivo dentro "Chapter I."

        f.writelines(chapter1)            # dara fuori tutto il testo
    
main()

# Riassunto: 
# Ho di nuovo aperto alice.txt in modalita lettura
# ho usato readlines() per accedere al contenuto come singole linee
# selezionato un sottoinsieme della lista usando lo slicing [:]
# utilizzato open in modalita scrittura per scrivere le linee in un nuovo file
