from numpy import numpy
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
