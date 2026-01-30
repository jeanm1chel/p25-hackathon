import numpy as np

class Grille:
    def __init__(self, n) :
        self.grille = np.empty((n,n,2))
        self.taille = n
    
    def voisin(self, (x,y)):
        L = []
        if x > 0 :
            L.append((x-1, y))
        if x < n:
            L.append((x+1,y))
        if y > 0:
            L.append((x, y-1))
        if y < n:
            L.append((x, y+1))
        return L
    
    def afficher(self):
        for ligne in self:
            text = ""
            for case in ligne:
                text.append