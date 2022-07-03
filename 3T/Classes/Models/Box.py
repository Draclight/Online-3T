class Box:
    def __init__(self, i, j):
        self.isSelected = False
        self.player = None
        self.value = "-"
        self.i = i
        self.set_j(j)
    
    def get_isSelected(self):
        return self.isSelected

    def set_isSelected(self, isSelected):
        self.isSelected = isSelected
    
    def get_player(self):
        return self.player

    def set_player(self, player):
        self.player = player

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def get_i(self):
        return self.i

    def set_i(self, i):
        self.i = i
    
    def get_j(self):
        return self.j

    def set_j(self, j):
        self.j = j