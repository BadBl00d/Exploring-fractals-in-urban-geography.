#BILBIOTHEQUES----------------------------
from PIL import Image, ImageTk 
import pylab as pl 
import  tkinter as Tk 
import numpy as np
import time
import Box_counting_1 as bc #PROGRAMME BOX COUNTING

#TKINTER
# Frame Tkinter
win = Tk.Tk()

#--------PARAMETRES À MODIFIER-------------
# Nombre d'étapes voulues
debut = 10 # Nombre d'itération du départ
valeur = 100 # Nombre d'itération final

# Image
picture = "SIERP.png" 

# Programme-----------------------------------
# Ouverture de l'image
image2 = Image.open(picture)
width2, height2 = image2.size

if width2 != height2: # Si l'image n'est pas carrée
    image = image2.crop((0, 0, min(width2, height2), min(width2, height2)))
    width, height = image.size  #taille 
else:
    image = image2
    width, height = image.size

image_gris= image.convert('L') # Nuances de gris
matrix_array = np.asmatrix(image_gris).copy() # Array
matrix = matrix_array.tolist() # Matrice de nuance de gris

# Image sur le canevas 
photo = ImageTk.PhotoImage(image) 
canvas = Tk.Canvas(win, width = image.size[0], height = image.size[1])
canvas.create_image(0,0, anchor = Tk.NW, image=photo)

canvas.pack()


#FONCTIONS
# Détection de pixel noir
def est_noir(t, a, b, side):
    color = 0 
    for y in range(b, b+side):
        for x in range(a, a+side): 
            if t[x][y]<150:# == 0: #< 150:  à modifier si image avec nuances de gris
                color+=1
    if color >=1: #si au moins un pixel dans ce bloc est noir
        return True

#création des boites tkinter 
def box():
    N = debut
    while N < valeur:
    # Nombre d'itérations = à modifier pour le nb de boites 
        side = int(height/(N+1)) #N+1
        liste = [int(height/(N+1))*_ for _ in range(N+1)]
        rectangle = []

        for y in liste:
            for x in liste:
                if est_noir(matrix, x, y, int(side)) == True : # Si au moins un pixel de la boite est noire
                    
                    id = canvas.create_rectangle(y, x, y+int(side), x+int(side), fill = 'blue')
                    rectangle.append(id)     
                else : 
                    id = canvas.create_rectangle(y, x, y+int(side) , x+int(side) , outline='blue')
                    rectangle.append(id)

        if N == valeur-1:# On s'arrete à l'étape d'avant pour laisser l'affichage
            break         
        else:             
            win.update()           
            time.sleep(.4)
            for k in range(len(rectangle)):
                canvas.delete(rectangle[k])
            rectangle.clear()
            win.update()
            N+=1   

# Box couting prompt
def prompt():
    var = bc.Box_counting(picture)
    text = Tk.Label(win, text = str(var))
    text.pack()

# Ajout de boutons 
# Boites
boxbutton = Tk.Button(win, text="Boites", fg="purple", command= box)
boxbutton.pack()

# Affichage de la dimension fractale
fracbutton = Tk.Button(win, text="Box counting", fg="blue", command=prompt )
fracbutton.pack()

quitbutton  = Tk.Button(win, text="Quitter", fg="red", command= quit)
quitbutton.pack()

win.mainloop()