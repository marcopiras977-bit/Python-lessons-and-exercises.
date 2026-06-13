# Approfondimento __init__ e self.

# Quando crei un nuovo oggetto da una classe, __init__ è la funzione che parte automaticamente e serve per inizializzare l'oggetto
# è come quando compri un telefono nuovo: la prima volta che lo accendi e fai la configurazione iniziale

class persona: 
    def __init__( self, nome):
        self.nome = nome
    
p = persona("Marco")    # qui parte in automatico __init__
print(p.nome)           # output : Marco 


# Self. è semplicemente il riferimento all' oggetto stesso
# " self è il modo con cui l'oggetto dice: ' sto parlando di ME' "

# self.nome = nome 

# nome : valore ricevuto "Marco"

# self.nome : il nome di quel oggetto 

# se non ci fosse Self. , Python non saprebbe dove salvare quel valore
