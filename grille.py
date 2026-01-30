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


    def voisins(self, pos, categorie):
        if categorie == "herbe":
            i = 1
        elif categorie == "animaux":
            i = 0
        else :
            i = 42 #génère erreur
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