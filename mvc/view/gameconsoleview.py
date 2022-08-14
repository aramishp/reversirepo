from view.gameview import GameView
from view.boardconsoleview import BoardConsoleView
from model.players import Players

class GameConsoleView(GameView):

    def __init__(self, game) -> None:
        super().__init__(game)
        self.boardview = BoardConsoleView(game.board)

    def display_board(self):
        self.boardview.display_board()

    def welcome_msg(self):
        super().welcome_msg()
        print('Welcome to Reversi')

    def win_msg(self, player):
        if player == Players.DRAW:
            print('Its a DRAW!')
        else:
            print(f'Congratulations {player}! You won')

    def your_turn_msg(self, player):
        print(f'Player {player}, is your turn')

    def invalid_place_msg(self):
        print('You cant put your piece there. Try Again')

    def get_position(self):
        while True: 
            try:
                location = input('Enter the location (x, y): ').split(',')
                x, y = int(location[0]), int(location[1])
                if (0 < x <= self.game.board.width) and (0 < y <= self.game.board.high):
                    return y-1, x-1
                print('Incorrect place, try again')
            except ValueError as e:
                print(e)
            except IndexError:
                print('This location is out of the board, try again')

    def display_score(self):
        print(f'Player X, your score is: {self.game.board.score(Players.RED_PLAYER)}')
        print(f'Player O, your score is: {self.game.board.score(Players.BLACK_PLAYER)}\n')

    def not_move_msg(self, player):
        print(f'Player {player}, you dont have possible moves.')

    def game_mode(self):
        while True:
            try:
                mode = int(input('Enter the game mode:\n1 - Player vs AI\n2 - Player vs Player\n'))
                if mode == 1 or mode == 2:
                    return mode
                print('Not an option, try again')
            except ValueError as e:
                print(e)

    def select_dif(self):
        while True:
            try:
                selection = int(input('Select the difficulty:\n1 - Easy\n2 - Medium\n3 - Hard\n'))
                if 0 < selection <= 3:
                    return selection - 1
                print('That is not an option, try again')
            except ValueError as e:
                print(e)
            
