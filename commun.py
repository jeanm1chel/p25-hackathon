import numpy as np
import math
import random as rd

from animals import Animals
from grass import Grass
from grille import Grille

n = 10
prob_repousse = 0.05
temps_repousse = 7

grille = Grille(n)
grass = Grass(prob_repousse, temps_repousse)

def mouvements(grille):
    for ligne in grille.matrice:
            for case in ligne:
                  case[0].move(grille)

def chasse(grille):
    for ligne in grille.matrice:
            for case in ligne:
                  case[0].eat_around(grille)


#incrémenter age
#MAJ herbe
mouvements(grille) # mouton #loups
chasse(grille) #loups
#vérif morts
#reprod
#affichage
# vérif condition d'arrêt