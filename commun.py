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
grass = Grass(grille, prob_repousse, temps_repousse)

def mouvements(grille):
    for ligne in grille:
            for case in ligne:
                  move(case[0])

def chasse(grille):
    for ligne in grille:
            for case in ligne:
                  eat_around(case[0])


#incrémenter age
#MAJ herbe
mouvements(grille) # mouton #loups
chasse(grille) #loups
#vérif morts
#reprod
#affichage
# vérif condition d'arrêt