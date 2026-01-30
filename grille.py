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


    def voisins_a(self, pos):
        x,y = pos
        n = self.taille
        L = []
        if x > 0 :
            L.append(self.matrice[x-1][y][i])
        if x < n-1:
            L.append(self.matrice[x+1][y][i])
        if y > 0:
            L.append(self.matrice[x][y-1][i])
        if y < n-1:
            L.append(self.matrice[x][y+1][i])
        return L
    
    def voisins_h(self, pos) :
        x,y = pos
        n = self.taille
        L = [] # liste des coordonées voisins
        G = [] # liste des coordonées où il y a de l'herbe
        if x > 0 :
            if self.matrice[x-1][y][1] == "#":
                G.append((x-1, y))
            else :
                L.append((x-1, y))
        if x < n-1:
            if self.matrice[x+1][y][1] == "#" :
                G.append((x+1,y))
            else :
                L.append((x+1,y))
        if y > 0:
            if self.matrice[x][y-1][1] == "#" :
                G.append((x, y-1))
            else :
                L.append((x, y-1))
        if y < n-1:
            if self.matrice[x][y+1][1] == "#" :
                G.append((x, y+1))
            else :
                L.append((x,y+1))
        return (L,G)
    
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