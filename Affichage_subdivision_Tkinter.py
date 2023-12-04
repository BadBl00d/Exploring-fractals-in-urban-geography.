#BILBIOTHEQUES
from PIL import Image, ImageTk 
import pylab as pl 
import  tkinter as Tk 
import numpy as np
import subdivision as recup

#TKINTER
# Tkinter frame
win = Tk.Tk()

#IMAGE
picture = "Paris3.png"
im = Image.open(picture)
bg = Tk.PhotoImage(file = picture)

# Image sur le canevas 
win.geometry(str(im.size[0])+'x'+str(im.size[1]))
label1 = Tk.Label(win, image = bg)
label1.place(x = 10, y = 0)


d = 70 # Taille des boites
u = recup.tableau_dimension(d, picture) # On récupère le tableau des dimensions obenu dans le module 'recup'

# Construction de la liste t
t = [] # On convertit la 'liste de liste' en une simple liste
for i in range(len(u)):
    t+=u[i]
t.pop(0)
t.append(0)

# Affichage des boites contenant la dimension fractale sur tkinter 
for i in range(len(t)):
    _ = recup.numero_vers_coordonnees(i,int(im.size[0]/d)) # On convertit le numéro de la boite en coordonnées de la boite
    label2 = Tk.Label( win, text = str(t[i]), relief = "raised" )
    label2.place(x = _[0]*d+int(d/2) , y = _[1]*d+int(d/2)) # On place la boite

win.mainloop()

