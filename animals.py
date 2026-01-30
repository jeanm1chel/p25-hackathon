import random
grille=[]

class Animals():

    def __init__(self,grille):
        self.type="W"
        self.position=(0,0)
        self.age=0
        self.energy=0

    def move(self):
        voisins=grille.voisins(self.position)
        if self.type=="W":
            if "S" in voisins:
                for voisin in voisins:
                    if voisin.type=="S":
                        self.position=voisin.position
                        break
            else :
                n=random.randint(len(voisins))
                self.position=voisins[n].position

        if self.type=="S":
            n=random.randint(len(voisins))
            self.position=voisins[n].position

    def eat_around(self):
        voisins=grille.voisins(self.position)
        if self.type=="W":
            for voisin in voisins:
                if voisin.type=="S":
                    self.eat(voisin)
        if self.type=="S":
            print("je suis un mouton je mange personne")

    
    def eat(self, cible):
        grille.grille[cible.position[0]][cible.position[1]]="."
        self.energy+=random.randint(30,40)

    def reproduction(self):
        voisins=grille.voisins(self.position)
        if self.energy > 80:
            for voisin in voisins:
                if voisin == ".":
                    voisin.type="W"
                    grille.update(voisin)
    
    


