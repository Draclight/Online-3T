from Classes.Models.Player import Player
from Classes.Models.Box import Box
import random

class Game:
    def __init__(self):
        self.players = []
        self.board = []
        self.isTermine = False
        self.nbCase = 3
        self.players.append(Player("p1", "X"))
        self.players.append(Player("p2", "O"))
        self.currentPlayer = self.players[self.get_random_first_player()]

        for i in range(self.nbCase):
            subBoard = []
            for j in range(self.nbCase):
                subBoard.append(Box(i, j))
            self.board.append(subBoard)

    def set_nbCase(self, nbCase):
        self.nbCase = nbCase
    
    def get_nbCase(self):
        return self.nbCase
    
    def get_random_first_player(self):
        return random.randint(0, 1)

    def swap_player_turn(self, player):
        if player.name == self.players[0].name:
            return self.players[1] 
        else:              
            return self.players[0] 

    def is_board_filled(self):
        for row in self.board:
            for item in row:
                if item.value == '-':
                    return False
        return True

    def show_board(self):
        for row in self.board:
            for item in row:
                print(item.value, end=" ")
            print()

    def player_play(self, row, col, player):
        box = self.board[row][col]
        if box.get_isSelected():
            return False
        else:
            box = player.play(box)
            self.board[row][col] = box
            return True

    def fix_spot(self, row, col, color):
        self.board[row][col].value = color

    def is_player_win(self, player):
        win = None
        n = len(self.board)

        # checking rows
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[i][j].value != player.color:
                    win = False
                    break
            if win:
                return win

        # checking columns
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[j][i].value != player.color:
                    win = False
                    break
            if win:
                return win

        # checking diagonals
        win = True
        for i in range(n):
            if self.board[i][i].value != player.color:
                win = False
                break
        if win:
            return win

        win = True
        for i in range(n):
            if self.board[i][n - 1 - i].value != player.color:
                win = False
                break
        if win:
            return win
        return False

    def start(self):
        while self.isTermine != True :
            print("Player", self.currentPlayer.name, "turn")
            self.show_board()
            isPlayValid = False

            """# taking user input
            row, col = list(map(int, input("Enter row and column numbers to fix spot: ").split()))
            print()
            # fixing the spot
            self.fix_spot(row - 1, col - 1, self.currentPlayer.color)
            """
            
            while isPlayValid != True:
                # taking user input
                row, col = list(map(int, input("Enter row and column numbers to fix spot: ").split()))
                if row < 1 :
                    print("row est invalide")
                elif row > 3:
                    print("row est invalide")
                elif col < 1:
                    print("col est invalide")
                elif col > 3:
                    print("col est invalide")
                else:
                    print()
                    # fixing the spot
                    isPlayValid = self.player_play(row - 1, col - 1, self.currentPlayer)

            isPlayValid = False
            # checking whether current player is won or not
            if self.is_player_win(self.currentPlayer):
                print(f"Player {self.currentPlayer.name} wins the game!")
                break

            # checking whether the game is draw or not
            if self.is_board_filled():
                print("Match Draw!")
                break

            # swapping the turn
            self.currentPlayer = self.swap_player_turn(self.currentPlayer)

        # showing the final view of board
        print()
        self.show_board()
    