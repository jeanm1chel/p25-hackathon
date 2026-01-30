import random as rd 
import numpy as np

class Animals():

    def __init__(self):
        self.type="."
        self.position=(0,0)
        self.age=0
        self.energy=0

    def move(self, grille):
        voisins_a = grille.voisins_a(self.position)
        voisins_h = grille.voisins_h(self.position)
        a, b = self.position[0], self.position[1]
        if self.type=="W":
            if "S" in voisins_a:
                for voisin in voisins_a:
                    if voisin.type=="S":
                        self.position=voisin.position
                        grille.matrice[voisin.position]=self
                        grille.matrice[a][b][0] = Animals()
                        break

            else :
                n=rd.randint(0, len(voisins_a)-1)
                x, y = voisins_a[n].position
                self.position = (x, y)
                grille.matrice[x][y][0]=self
                grille.matrice[a][b][0] = Animals()

        if self.type=="S":
            if len(voisins_h[1]) != 0 :
                n = rd.randint(0,len(voisins_h[1])-1)
                x, y = voisins_h[1][n][0], voisins_h[1][n][1]
                self.position = (x, y)
                grille.matrice[x][y][0]=self
                grille.matrice[a][b][0] = Animals()

            else :
                n = rd.randint(0,len(voisins_h[0])-1)
                x, y = voisins_h[0][n][0], voisins_h[0][n][1]
                self.position = (x, y)
                grille.matrice[x][y][0]=self
                grille.matrice[a][b][0] = Animals()

    def mort(self, grille):
        self.type="."
        self.age=0
        self.energy=0
        x, y = self.position
        grille.matrice[x][y][0]=self

    def reproduction(self, grille):
        voisins=grille.voisins_a(self.position)
        if self.type == "W":
            if self.energy > 80:
                for voisin in voisins:
                    if voisin == ".":
                        voisin.type="W"
                        voisin.age=0
                        voisin.energy=20
                        self.energy-=20
                        grille.grille[voisin[0].position]=voisin
                        break
        if self.type == "S":
            if self.energy > 50:
                for voisin in voisins:
                    if voisin == ".":
                        voisin.type="S"
                        voisin.age=0
                        voisin.energy=20
                        self.energy-=20
                        grille.grille[voisin.position]=voisin
                        break


def animals_initialize(grille_vide, n_W=10, n_S=50):
    li_xy=[]
    for i in range(np.shape(grille_vide)[0]):
        for j in range( np.shape(grille_vide)[1]):
            li_xy.append((i,j))
    print(li_xy)
    n=np.shape(grille_vide)[0]*np.shape(grille_vide)[1]
    for _ in range (n_W):
        pos=li_xy[rd.randint(0,n-1)]
        grille_vide[pos[0]][pos[1]][0].type="W"
        grille_vide[pos[0]][pos[1]][0].position=pos
        grille_vide[pos[0]][pos[1]][0].energy=40
        grille_vide[pos[0]][pos[1]][0].age=0
        li_xy.remove(pos)
        n-=1
    for _ in range (n_S):
        pos=li_xy[rd.randint(0,n-1)]
        grille_vide[pos[0]][pos[1]][0].type="S"
        grille_vide[pos[0]][pos[1]][0].position=pos
        grille_vide[pos[0]][pos[1]][0].energy=40
        grille_vide[pos[0]][pos[1]][0].age=0
        li_xy.remove(pos)
        n-=1
        
    return(grille_vide)
        
            