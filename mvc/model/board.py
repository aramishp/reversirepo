from pickle import EMPTY_DICT
from model.players import Players

class Board:
    EMPTY_CELL = ' '

    def __init__(self, high, width) -> None:
        self.high = high
        self.width = width
        self.create_board()

    def create_board(self):
        self.mat = [[self.EMPTY_CELL] * self.width for _ in range(self.high)]
        self.mat[self.width//2-1][self.high//2-1] = Players.BLACK_PLAYER
        self.mat[self.width//2][self.high//2] = Players.BLACK_PLAYER
        self.mat[self.width//2-1][self.high//2] = Players.RED_PLAYER
        self.mat[self.width//2][self.high//2-1] = Players.RED_PLAYER

    def get_cell(self, row, col):
        return self.mat[row][col]

    def update_cell(self, row, col, player):
        self.mat[row][col] = player

    #Return the score of one player
    def score(self, player: Players):
        score = 0
        for i in range(self.width):
            for j in range(self.high):
                if self.mat[i][j] == player:
                    score +=1
        return score

    #Print the board in a open file
    def print_board(self, dest):
        for i in range(self.high):
            print(self.mat[i], file = dest)
        print(file=dest)


    def print_board2(self):
        for i in range(self.high):
            for j in range(self.width):
                print(self.mat[i][j], end=' ') 
            print()