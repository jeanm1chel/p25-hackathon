RESET    = "\033[0m"     
GREEN_BG = "\033[42m"     # fond vert (herbe)

def afficher(grille, n):
    for i in range(n):
        ligne = ""

        for j in range(n):

            animal = grille.grille[i][j][0]   # objet a
            herbe  = grille.grille[i][j][1]   # "#" ou "."

            #CASE AVEC HERBE
            if herbe == "#":

                if animal.type == ".":  
                    ligne += GREEN_BG + " " + RESET
                else:
                    ligne += GREEN_BG + animal.type + RESET

            #CASE SANS HERBE
            else:

                if animal.type == ".":  
                    ligne += "."
                else:
                    ligne += animal.type
                    
        print(ligne)