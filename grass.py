import math
import random as rd

class Grass:
    def __init__(self, prob_pousse, temps_repousse) :
        self.herbe = []
        self.prob_pousse = prob_pousse
        self.temps_repousse = temps_repousse
        self.herbe_mangé = {}
    
    def initialisation(self, grille) :
        C = 0
        n = len(grille.matrice)
        nb_grass = math.floor(0.3*(n)**2)
        while C < nb_grass :
            x = rd.randint(0, n-1)
            y = rd.randint(0, n-1)
            if (x,y) not in self.herbe :
                self.herbe.append((x,y))
                C += 1
                grille.matrice[x][y][1] = "#"
        
    def nouvelle_herbe(self, grille) :
        n = grille.taille
        for i in range(n) :
            for j in range(n) :
                if (i,j) not in (self.herbe and self.herbe_mangé) :
                    m = rd.uniform()
                    if m < self.prob_repousse :
                        self.append((i,j))
                        grille.matrice[i][j][1] = "#"

    def mangé(self, grille) :
        for i in range(len(self.herbe)) :
            x = self.herbe[i][0]
            y = self.herbe[i][1]
            if grille.matrice[x, y, 0] == "S" :
                self.herbe_mangé[(x,y)] = 0
                self.herbe.pop(i)
                
    def repousse_herbe(self) : #le faire tout à la fin car réinitialise direct pour le prochain
        for c in self.herbe_mangé :
            self.herbe_mangé[c] += 1
            if self.herbe_mangé == self.temps_repousse :
                self.herbe.append(c)
                self.Grille.grille[c[0]][c[1]][1] = "#"
                del self.herbe_mangé[c]
            

        
    
