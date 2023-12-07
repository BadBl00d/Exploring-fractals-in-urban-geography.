# Import bibliothèques
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def est_noir(image, epsilon):
    height, width = image.shape
    s = 0 # Nombre de boites contenant un pixel noir

    # Parcours de l'image avec une taille de boîte donnée
    for i in range(0, height - epsilon + 1, epsilon):
        for j in range(0, width - epsilon + 1, epsilon):
            box = image[i:i+epsilon, j:j+epsilon]
            if np.sum(box) > 0:
                s += 1
    return s

def box_counting(image, min_epsilon, max_epsilon, num_boites):
    boites = np.logspace(np.log10(min_epsilon), np.log10(max_epsilon), num_boites, dtype=int)
    boxes = []

    # Calcul du nombre de boîtes pour chaque taille de boîte
    for boite in boites:
        count = est_noir(image, boite)
        boxes.append(count)

    box_counts = np.array(boxes)
    boites = np.array(boites)

    # Régression linéaire pour estimer la dimension fractale
    coeffs = np.polyfit(np.log(boites), np.log(box_counts), 1)
    dimension = -coeffs[0]

    return dimension

# Utilisation
chemin_image = 'SIERPINSKI.png'  #fichier image
min_epsilon = 1
max_epsilon = 100
num_boites = 10

# Ouverture de l'image à l'aide de PIL
image = Image.open(chemin_image).convert('L')  # Conversion en niveaux de gris
image = np.array(image)

dimension = box_counting(image, min_epsilon, max_epsilon, num_boites)
print("Dimension fractale de "+chemin_image+':', dimension)
