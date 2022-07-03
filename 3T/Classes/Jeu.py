from Classes.Models.Case import Case
from Classes.Models.Joueur import Joueur

import random

class Jeu:
    def __init__(self):
        self.joueurs = []
        self.tableau = []
        self.isTermine = False
        self.nbCase = 3
        self.joueurs.append(Joueur("J1", "croix"))
        self.joueurs.append(Joueur("J2", "rond"))

        for i in range(self.nbCase):
            subTableau = []
            for j in range(self.nbCase):
                subTableau.append(Case(i, j))
            self.tableau.append(subTableau)

    def set_nbCase(self, nbCase):
        self.nbCase = nbCase
    
    def get_nbCase(self):
        return self.nbCase
        
    def start(self):
        j1:Joueur = self.joueurs[0]
        j2:Joueur = self.joueurs[1]
        while self.isTermine != True :
            j1.jouer()
            j2.jouer()
            self.isTermine = self.victoire()
    
    def victoire(self):
        tableau = self.tableau
        vic = False
        print('longueur tab: ', len(tableau))
        for i in  range(len(tableau)):
            subTableau = tableau[i]
            for j in  range(len(subTableau)):
                case:Case = (subTableau[j])[0]   
                print('i: ', case.i, ' - j: ', case.j)

        for ligeTab in range(len(tableau)):
            subTableau = tableau[ligeTab]
            nbCaseSelected = 0
            for colOfLine in range(len(subTableau)):
                case:Case = subTableau[colOfLine]
                if case.isSelected :
                    nbCaseSelected = nbCaseSelected + 1
                else:
                    break
        
            if nbCaseSelected == 3 :
                vic = True
                break

        return vic
