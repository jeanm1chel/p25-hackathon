import random as rd 
import numpy as np

class Animals():

    def __init__(self):
        self.type="."
        self.position=(0,0)
        self.age=0
        self.energy=0

    def move(self, grille):
        voisins=grille.voisins(self.position, "animaux")
        if self.type=="W":
            if "S" in voisins:
                for voisin in voisins:
                    if voisin.type=="S":
                        self.position=voisin.position
                        grille.grille[voisin.position]=self
                        break
            else :
                n=rd.randint(0, len(voisins)-1)
                x, y = voisins[n].position
                self.position = (x, y)
                grille.matrice[x][y][0]=self

        if self.type=="S":
            n=rd.randint(0,len(voisins)-1)
            x, y = voisins[n].position
            self.position = (x, y)
            grille.matrice[x][y][0]=self

    def mort(self, grille):
        self.type="."
        self.age=0
        self.energy=0
        grille.grille[self.position]=self

    def eat_around(self, grille):
        voisins=grille.voisins(self.position)
        if self.type=="W":
            for voisin in voisins:
                if voisin[0].type=="S":
                    self.eat(voisin)
                    voisin[0].mort(grille)
                
        if self.type=="S":
            print("je suis un mouton je mange personne")

    
    def eat(self, cible, grille):
        grille.matrice[cible.position[0]][cible.position[1]]="."
        self.energy+=rd.randint(30,40)

    def reproduction(self, grille):
        voisins=grille.voisins(self.position)[0]
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
        
            