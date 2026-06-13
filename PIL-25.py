# PIL pillow.readthedocs.io --------------------------------------------------------------

# creare un programma che fa le GIF 

# in un file: "costume1.gif" (ce 1 immagine)
# in un file: "costume2.gif" (ce 1 immagine)
# in un file: "costumes.py" (ce il programma che crea la GIF)

import sys

from PIL import Image

images = []

for arg in sys.argv[1:]: # sys.argv è una lista che contiene gli argomenti passati al programma da riga di comando. sys.argv[0] è il nome del programma stesso, quindi sys.argv[1:] contiene tutti gli argomenti successivi.
    image= Image.open(arg)
    images.append(image)

images[0].save(
    "costume.gif",save_all=True, append_images=[images[1]],duration= 200, loop= 0
) 
# images[0].save() : salva la prima immagine come costume.gif, e le altre immagini vengono aggiunte alla GIF come fotogrammi successivi, con una durata di 200 millisecondi tra ogni fotogramma.
# loop=0 : indica che la GIF deve essere riprodotta in loop infinito.

# P.S. output sarà errore perhe non ci sono i file costume1.gif e costume2.gif, ma se ci fossero, il programma funzionerebbe correttamente.



# ----------------------------------------------------------------------------------------------------
# PILLOW shorts:

# in un file "in.jpeg" (ce un'immagine)

# creiamo iun file "image.py" con questo codice:

from PIL import Image

def main():
    with Image.open("in.jpeg") as img:
        print(img.size) # stampa la dimensione dell'immagine in pixel (larghezza, altezza)
        print(img.format) # stampa il formato dell'immagine (ad esempio, JPEG, PNG, etc.)
        img = img.rotate(180) # ruota l'immagine di 180 gradi (puoi specificare altri angoli come 90, 270, etc.)
        img.save("out.jpeg") # salva l'immagine modificata con un nuovo nome (out.jpeg)

main()

# per applicare un filtro 

from PIL import Image, ImageFilter

def main():
    with Image.open("in.jpeg") as img:
        img = img.filter(ImageFilter.BLUR) # applica un filtro di sfocatura all'immagine (puoi scegliere altri filtri come ImageFilter.CONTOUR, ImageFilter.DETAIL, etc.)
        img = img.filter(ImageFilter.FIND_EDGES) # applica un filtro per evidenziare i bordi dell'immagine
        img.save("out.jpeg") # salva l'immagine modificata con un nuovo nome (out.jpeg)

main()