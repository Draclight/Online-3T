class Case:
    def __init__(self, i, j):
        self.isSelected = False
        self.joueur = None
        self.valeur = None
        self.i = i
        self.set_j(j)
    
    def get_isSelected(self):
        return self.isSelected

    def set_isSelected(self, isSelected):
        self.isSelected = isSelected
    
    def get_joueur(self):
        return self.joueur

    def set_joueur(self, joueur):
        self.joueur = joueur

    def get_valeur(self):
        return self.valeur

    def set_valeur(self, valeur):
        self.valeur = valeur

    def get_i(self):
        return self.i

    def set_i(self, i):
        self.i = i
    
    def get_j(self):
        return self.j

    def set_j(self, j):
        self.j = j