import numpy as np
import math
import random as rd

from animals import Animals
from grass import Grass
from grille import Grille

n = 10
prob_pousse = 0.05
temps_repousse = 7
age_limite_mouton = 50
age_limite_loup = 40

grille = Grille(n)
grass = Grass(prob_pousse, temps_repousse)

def mouvements(grille):
    for ligne in grille.matrice:
            for case in ligne:
                  case[0].move(grille)

def chasse(grille):
    for ligne in grille.matrice:
            for case in ligne:
                  case[0].eat_around(grille)

def vieillissement_et_mort(grille) :
    for ligne in grille.matrice :
        for case in ligne :
            if case[0].type != "." :
                case[0].age += 1
                if case[0].age == age_limite_loup and case[0].type == "W" :
                    case[0].type = "."

grass.initialisation(grille)

for i in range(500):
    #incrémenter age
    #MAJ herbe
    mouvements(grille) # mouton #loups
    chasse(grille) #loups
    vieillissement_et_mort(grille) #vérif morts
    #reprod
    grille.afficher() #affichage
    # vérif condition d'arrêt