# Import bibliothèque
from PIL import Image 
import numpy as np
import pylab as pl 
import time

def Box_counting(image_mat): 
    # Chronomètre
    t_debut = time.time() 

    image = Image.open(image_mat)  # Création d'une matrice 
    image_gris = image.convert('L')   # Conversion en nuances de gris
    
    image_matrix = np.asmatrix(image_gris).copy()  # Adaptation numpy 

    
    thresh = 128  # 0:pixel noir - 255:pixel blanc -> valeur du tresholding

    for i in range(image.size[1]): # Hauteur
        for j in range(image.size[0]): # Largeur
            if image_matrix[i,j] > thresh:
                image_matrix[i,j] = 255    # Blanc
            else:
                image_matrix[i,j] = 0   # Noir

    # Liste des coordonnées de pixel noirs
    liste_pixel=[]                                                  
    for i in range(image.size[1]):
        for j in range(image.size[0]):
            if image_matrix[i,j] == 0:  #  Le pixel est noir
                liste_pixel.append((i,j))    #  Ajout du pixel dans la matrice 

    Lx=image_gris.size[0]
    Ly=image_gris.size[1]
    pixels_matrice=pl.array(liste_pixel)   # Conversion pylab array
    
    # On ne considère que l'échelle logarithmique
    echelles=np.logspace(1, 8, num=20, endpoint=False, base=2) #ln(2)
    
    Ns=[]
    
    # Boucle de 'plusieurs échelles' 
    for echelle in echelles:
        print ('======= Échelle :', echelle)
        # Graphe
        H, edges=np.histogramdd(pixels_matrice, bins=(np.arange(0,Lx,echelle),np.arange(0,Ly,echelle)))       
        Ns.append(np.sum(H > 0))
    
    # Regression linéaire
    coeffs=np.polyfit(np.log(echelles), np.log(Ns), 1)
    
    D = round(-coeffs[0], 3) # Opposé de la pente
    
    # Style tracé
    pl.plot(np.log(echelles),np.log(Ns), 'o', mfc='none', label='data')  
    pl.plot(np.log(echelles), np.polyval(coeffs,np.log(echelles)),label='fit') #Régression
    pl.xlabel('log $\epsilon$') # Taille de la boîte considérée 
    pl.ylabel('log N') 
    pl.title( image_mat +' D = '+str(D)) 
    pl.show() 

    # Stop chronomètre
    temps = time.time()-t_debut 

    return (D, round(temps, 3) )
    
print(Box_counting('SIERPINSKI.png'))
