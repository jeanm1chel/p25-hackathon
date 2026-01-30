import math
import random as rd

class Grass:
    def __init__(self, Grille, prob_pousse, temps_repousse) :
        self.Grille = Grille
        self.herbe = []
        self.prob_pousse = prob_pousse
        self.temps_repousse = temps_repousse
        self.herbe_mangé = {}
    
    def initialisation(self) :
        C = 0
        nb_grass = math.floor(0.3*(len(self.grille))**2)
        while C < nb_grass :
            x = rd.randint(0, len(self.grille))
            y = rd.randint(0, len(self.grille))
            if (x,y) not in self.coord :
                self.herbe.append((x,y))
                C += 1
                self.Grille.grille[x,y,1] = "#"
        
    def nouvelle_herbe(self) :
        for i in range(n) :
            for j in range(n) :
                if (i,j) not in self.herbe :
                    m = rd.uniform()
                    if m < self.prob_repousse :
                        self.append((i,j))
                        self.Grille.grille[i,j,1] = "#"

    def repousse_herbe(self) : #le faire tout à la fin car réinitialise direct pour le prochain
        for c in self.herbe_mangé :
            self.herbe_mangé[c] += 1
            if self.herbe_mangé == self.temps_repousse :
                self.herbe.append(c)
                self.Grille.grille[c[0], c[1],1] = "#"
                del self.herbe_mangé[c]
            

        
    
