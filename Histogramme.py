{python}

#BILI
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
import numpy as np
import subdivision as recup 

d = 5 # Taille des 'sous-images'

#issu de : https://matplotlib.org/stable/tutorials/colors/colormap-manipulation.html#sphx-glr-tutorials-colors-colormap-manipulation-py

'''Prend en entrée colormaps: une palette de couleur dans le module cmp'''

def plot_examples(colormaps):
    name = 'Paris.png'
    data = recup.tableau_dimension(d, name) # Nombre de carrés
    n = len(colormaps)
    fig, axs = plt.subplots(1, n, figsize=(n * 2 + 2, 3),
                            constrained_layout=True, squeeze=False)
    for [ax, cmap] in zip(axs.flat, colormaps):
        psm = ax.pcolormesh(data, cmap=cmap, rasterized=True, vmin=0, vmax=2.2) # Plage de variation des couleurs
        fig.colorbar(psm, ax=ax)
    plt.title('Paris et sa banlieue')
    plt.show()

viridis = mpl.colormaps['jet'].resampled(256) 

plot_examples([viridis])
