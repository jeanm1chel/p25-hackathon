import numpy as np
from animals import Animals

class Grille:
    def __init__(self, n) :
        self.taille = n
        self.matrice = []
        for i in  range(n):
            ligne = []
            for j in range(n):
                ligne.append([Animals(), "."])
            self.matrice.append(ligne)
    
    def voisin(self, pos):
        x,y = pos
        L = []
        if x > 0 :
            L.append(self[x-1, y])
        if x < n:
            L.append(self[x+1,y])
        if y > 0:
            L.append(self[x, y-1])
        if y < n:
            L.append(self[x, y+1])
        return L
    
    def afficher(self):
        text = ""
        for ligne in self.matrice:
            for case in ligne :
                if case[0].type != "." :
                    text += case[0].type
                elif case[1] == "#" :
                    text += case[1]
                else :
                    text += "."
            text += "\n"
        print(text)