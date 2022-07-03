class Joueur:
    def __init__(self, name, couleur):
        self.name = name
        self.couleur = couleur
    
    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.couleur

    def set_couleur(self, couleur):
        self.couleur = couleur

    def jouer(self, case):
        case.set_isSelected(True)
        case.set_joueur(self)