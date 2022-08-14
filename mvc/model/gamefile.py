from datetime import datetime
from model.players import Players
from model.board import Board

class Gamefile:
    
    def __init__(self, file_path, winner, board: Board) -> None:
        self.file_path = file_path
        self.board = board
        self.winner = winner

    #Put the date, time, winner, board and the score of both players
    def game_file(self):
        with open(self.file_path, 'w') as f:
            now = datetime.now()
            print(now.strftime('%d-%m-%Y %H:%M:%S'), end='\n\n', file=f)
            if self.winner != Players.DRAW:
                print(f'Congratulations! You won player {self.winner}!', end='\n\n', file=f)
            else:
                print('Its a Draw!', end='\n\n', file=f)
            self.board.print_board(f)
            print(f'Player {Players.RED_PLAYER} your score is {self.board.score(Players.RED_PLAYER)}', file=f)
            print(f'Player {Players.BLACK_PLAYER} your score is {self.board.score(Players.BLACK_PLAYER)}', file=f)
            