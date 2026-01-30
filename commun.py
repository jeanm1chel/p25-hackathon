import numpy as np
import math
import random as rd
import time

from animals import Animals, animals_initialize
from grass import Grass
from grille import Grille

n = 10
prob_pousse = 0.05
temps_repousse = 7
age_limite_mouton = 50
age_limite_loup = 40
nrj_loss_sheep = 1
nrj_loss_wolf = 2

grille = Grille(n)
grass = Grass(prob_pousse, temps_repousse)
grass.initialisation(grille)
grille.matrice= animals_initialize(grille.matrice)


def mouvements(grille):
    for ligne in grille.matrice:
            for case in ligne:
                  case[0].move(grille)

def chasse(grille):
    for ligne in grille.matrice:
            for case in ligne:
                  case[0].eat_around(grille)

def naissances(grille):
    for ligne in grille.matrice:
            for case in ligne:
                  case[0].reproduction(grille)

def referendum(grille):
    nb_vivants = 0
    for ligne in grille.matrice:
            for case in ligne:
                if case[0].type != ".":
                    nb_vivants += 1
    return nb_vivants

def vieillissement_et_mort(grille, age_limite_loup, age_limite_mouton) :
    for ligne in grille.matrice :
        for case in ligne :
            if case[0].type != "." :
                case[0].age += 1
                if (case[0].age == age_limite_loup or case[0].energy <= 0) and case[0].type == "W" :
                    case[0].type = "."
                    case[0].energy = 0
                    case[0].age = 0
                elif (case[0].age == age_limite_mouton or case[0].energy <= 0) and case[0].type == "S"
                    case[0].type = "."
                    case[0].energy = 0
                    case[0].age = 0

def loss_energy(grille) :
    for ligne in grille.matrice:
            for case in ligne:
                if case[0].type == "W" :
                    case[0].energy -= nrj_loss_wolf
                elif case[0].type == "S" :
                    case[0].type -= nrj_loss_sheep
                


for i in range(500):
    loss_energy(grille)
    grass.nouvelle_herbe(grille)#MAJ herbe
    grass.repousse_herbe(grille)
    mouvements(grille) # mouton #loups
    chasse(grille) #loups
    vieillissement_et_mort(grille) #incrémenter age  #vérif morts
    naissances(grille) #reprod
    grille.afficher() #affichage
    if referendum(grille) <= 0:
        break# vérif condition d'arrêt
    time.sleep(0.5)