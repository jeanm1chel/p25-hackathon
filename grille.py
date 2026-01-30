import numpy as np
from animals import Animals

class Grille:
    def __init__(self, n) :
        self.taille = n
        self.matrice = [[[Animals(), "."] for _ in range(n)] for _ in range(n)]

        
    def mattoshow(self):
        n=self.taille
        mat=[[[0,0] for _ in range (n)] for _ in range (n)]
        for i in range(n):
            for j in range(n):
                mat[i][j]=[self.matrice[i][j][0].type, self.matrice[i][j][1]]
        return mat


    def voisins(self, pos):
        x,y = pos
        n = self.taille
        L = []
        if x > 0 :
            L.append(self.matrice[x-1][y])
        if x < n-1:
            L.append(self.matrice[x+1][y])
        if y > 0:
            L.append(self.matrice[x][y-1])
        if y < n-1:
            L.append(self.matrice[x][y+1])
        return L
    
    def afficher(self):
        text = ""
        for ligne in self.matrice:
            for case in ligne :
                if case[0].type != "." :
                    text += " " + case[0].type + " "
                elif case[1] == "#" :
                    text += " " + case[1] + " "
                else :
                    text += " . "
            text += "\n"
        print(text)