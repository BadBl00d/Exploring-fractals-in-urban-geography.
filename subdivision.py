# Import bibli
from PIL import Image
from itertools import product
import numpy as np
import pylab as pl
import time
import os

'''version qui prend en entrée le format image PIL. Box counting renvoit la dimension fractale d'une image. tile() prend en entrée une image et subdivise cette image en images de coté d.  Puis, dans la même boucle, on applique l'algorithme de Box counting à chaque subdivision créée. 

Le dictionnaire renvoyé contient les dimensions fractales de chaque boite, de bas en haut et de gauche à droite (l'origine se situant au coin supérieur gauche). '''


def Box_counting1(image): 

    d = {} 
    t_debut = time.time() #chronomètre 

    image_grayscale = image.convert('L')   # on la convertit en nuances de gris
    
    image_matrix = np.asmatrix(image_grayscale).copy()  #adaptation numpy 
    
    
    thresh = 0 # 0;black 255:white // valeur arbitrire du tresholding
    
    for i in range(image.size[1]): #hauteur
        for j in range(image.size[0]): #largeur
            if image_matrix[i,j] > thresh:
                image_matrix[i,j] = 255    # blanc
            else:
                image_matrix[i,j] = 0   # noir
    
    # liste des coordonnées de pixel noirs
    pixels=[]                                                  
    for i in range(image.size[1]):
        for j in range(image.size[0]):
            if image_matrix[i,j] == 0:  #  pixel is black
                pixels.append((i,j))    #  on le compte
    Lx=image_grayscale.size[0]
    Ly=image_grayscale.size[1]
    
    pixels=pl.array(pixels)   # conversion pylab array

    if len(pixels)!=0:
        scales=np.logspace(1, 8, num=20, endpoint=False, base=2) #ln(2)
    
        Ns=[]
        
        #boucle de plusieurs echelles 
        for scale in scales:
            #print ('======= Scale :', scale)  #vérif à virer 
            
            #graphe
            H, edges=np.histogramdd(pixels, bins=(np.arange(0,Lx,scale),np.arange(0,Ly,scale)))       
            Ns.append(np.sum(H > 0))
        
        a = np.log(scales)
        u = a.tolist()

        for i in range(len(Ns)):
            if 0 in Ns:
                Ns.remove(0)
                u.pop(-1)
        
        fin  = np.array(u)
        # regression linéaire
        coeffs=np.polyfit(fin, np.log(Ns), 1)
        
        D = round(-coeffs[0], 3) # oppose de la pente
        d['dim'] = D
        
    
    else:
        d['dim']=0
    temps = time.time()-t_debut #stop chrono
    #affichage
    d['temps'] = round(temps, 4)
    return d

def tile(d, name):
    img = Image.open(name)
    w, h = img.size

    l = {}
    count  = 1
    grid = product(range(0, h-h%d, d), range(0, w-w%d, d))
    for i, j in grid:
        box = (j, i, j+d, i+d)
        a = img.crop(box) # On divise l'image en boites de coté d
        u = Box_counting1(a) # On applique un algorithme de box counting à chacune d'entre elles
        l[str(count)] = u # On ajoute la dim dans un dico (clef = indice)
        count+=1
        
    return l, w #renvoit le dico des dimensions 

