from grille import Grille
from animals import Animals, animals_initialize
import numpy as np
grille = Grille(20)
print(grille.matrice)
print(np.shape(grille.matrice))
print(grille.mattoshow())
grille.matrice= animals_initialize(grille.matrice)
print(grille.mattoshow())
