class Player:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    
    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.color

    def set_color(self, color):
        self.color = color

    def play(self, case):
        case.set_isSelected(True)
        case.set_player(self)