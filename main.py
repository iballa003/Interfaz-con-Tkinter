from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os
import random

listaImagenes = os.listdir("./hiragana")
listaAleato = random.choice(listaImagenes)
listaAleatoSinExt = listaAleato.split(".")[0]
contador = 0
listaImagenUsadas = []

def comprobarInput():
    global contador
    if entry.get() == listaAleatoSinExt:
        print("Correcto")
        contador += 1
    else:
        print("Incorrecto")
    #listaImagenUsadas.append(listaAleato)
    cambiarImagen()

def cambiarImagen():
    global listaAleatoSinExt
    listaAleato2 = random.choice(listaImagenes)
    print(listaImagenUsadas)
    if listaAleato2 in listaImagenUsadas: 
        print("exist")
        cambiarImagen()
    else: 
        print("not exist")
        listaImagenUsadas.append(listaAleato2)
        
    image2 = ImageTk.PhotoImage(Image.open("hiragana/"+listaAleato2))
    image_label.configure(image=image2)
    image_label.im=image2
    listaAleatoSinExt = listaAleato2.split(".")[0]
    print(listaAleatoSinExt)    
      
root = Tk()
root.geometry("200x300")
image = ImageTk.PhotoImage(Image.open("hiragana/"+listaAleato))
# Create a label to display the image
image_label = ttk.Label(root, image=image,width=60,padding=10)
image_label.pack()
entry = ttk.Entry()
entry.pack(padx=10,pady=10)
button = ttk.Button(root, text="Comprobar", command = comprobarInput)
button.pack()
button2 = ttk.Button(root, text="Salir", command=root.destroy)
button2.pack()
root.mainloop()