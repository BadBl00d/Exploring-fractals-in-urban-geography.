#Ce programme permet la dilatation d'une image 
# adapté de: https://openclassrooms.com/fr/courses/5060661-initiez-vous-aux-traitements-de-base-des-
# images-numeriques/5217276-maitrisez-les-operations-morphologiques-de-base

# Import bibli
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# Fonctions -----------------------------------------
def convolution (image,filtre,function):
    new_image = np.zeros(image.shape, int)
    for i in range(0,image.shape[0]):
        for j in range(0,image.shape[1]):
            new_image[i,j] = function(image,i,j,filtre)
    return new_image

# Dilatation
def pixel_erosion(image, ligne, colonne, elmt_structurant):

    width = len(elmt_structurant) // 2
    height = len(elmt_structurant[0]) // 2
    pixel_value = True;

    for i in range(0,len(elmt_structurant)):
        for j in range(0,len(elmt_structurant[0])):
            x_image = ligne + i - width
            y_image = colonne + j - height

            if((x_image >= 0) and (x_image < image.shape[0]) and (y_image>=0) and (y_image<image.shape[1])):
                if (elmt_structurant[i,j] and not(image[x_image,y_image])):
                    pixel_value = False

    return pixel_value

def erosion(image, elmt_structurant):
    return convolution(image,elmt_structurant,pixel_erosion)

def ero(image):
    return erosion(image, filtre)

#  Image et filtre
image = cv.imread('18e.png',0)
filtre = np.array([[0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [1, 1, 1, 1, 1], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0]])

'''
Filtre de la forme : 
[[0 0 1 0 0]
 [0 0 1 0 0]
 [1 1 1 1 1]
 [0 0 1 0 0]
 [0 0 1 0 0]]

'''

# Affichage matplotlib
objet  = ero(image)

plt.figure()
plt.imshow(objet,cmap='gray')
plt.show()

