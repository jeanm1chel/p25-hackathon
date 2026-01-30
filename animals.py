import random as rd 
import numpy as np

class Animals():

    def __init__(self):
        self.type="."
        self.position=(0,0)
        self.age=0
        self.energy=0

    def move(self, grille):
        voisins=grille.voisins(self.position)
        if self.type=="W":
            if "S" in voisins:
                for voisin in voisins:
                    if voisin.type=="S":
                        self.position=voisin.position
                        grille.grille[voisin.position]=self
                        break
            else :
                n=rd.randint(len(voisins))
                self.position=voisins[n].position
                grille.grille[voisin[n].position]=self

        if self.type=="S":
            n=rd.randint(len(voisins))
            self.position=voisins[n].position
            grille.grille[voisins[n].position]=self

    def mort(self, grille):
        self.type="."
        self.age=0
        self.energy=0
        grille.grille[self.position]=self

    def eat_around(self, grille):
        voisins=grille.voisins(self.position)
        if self.type=="W":
            for voisin in voisins:
                if voisin.type=="S":
                    self.eat(voisin)
                    voisin.mort(grille)
                
        if self.type=="S":
            print("je suis un mouton je mange personne")

    
    def eat(self, cible, grille):
        grille.matrice[cible.position[0]][cible.position[1]]="."
        self.energy+=rd.randint(30,40)

    def reproduction(self, grille):
        voisins=grille.voisins(self.position)
        if self.energy > 80:
            for voisin in voisins:
                if voisin == ".":
                    voisin.type="W"
                    voisin.age=0
                    voisin.energy=20
                    self.energy-=20
                    grille.grille[voisin.position]=voisin


    def animals_initialize(grille_vide, n_W=10, n_S=50):
        li_xy=[]
        for i in range(np.shape(grille_vide)[0]):
            for j in range( np.shape(grille_vide)[1]):
                li_xy.append(i,j)
        n=np.shape(grille_vide)[0]*np.shape(grille_vide)[1]
        for _ in range (n_W):
            pos=li_xy[rd.randint(0,n)]
            grille_vide[pos[0]][pos[1]].type="W"
            grille_vide[pos[0]][pos[1]].position=pos
            grille_vide[pos[0]][pos[1]].energy=40
            grille_vide[pos[0]][pos[1]].age=0
            li_xy.remove(pos)
            n-=1
        for _ in range (n_S):
            pos=li_xy[rd.randint(0,n)]
            grille_vide[pos[0]][pos[1]].type="W"
            grille_vide[pos[0]][pos[1]].position=pos
            grille_vide[pos[0]][pos[1]].energy=40
            grille_vide[pos[0]][pos[1]].age=0
            li_xy.remove(pos)
            n-=1
        
        
            