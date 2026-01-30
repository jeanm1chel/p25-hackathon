import numpy as np

class Grille:
    def __init__(self, n) :
        self.taille = n
        self.grille = np.empty((n,n,2))
        for ligne in self:
            for case in ligne:
                case[0] = animals()
                case[1] = grass()
    
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
        for ligne in self:
            text = ""
            for case in ligne:
                text.append