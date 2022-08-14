from abc import ABC, abstractmethod
from model.game import Game

class GameView(ABC):

    def __init__(self, game: Game) -> None:
        self.game = game

    @abstractmethod    
    def welcome_msg(self):
        pass

    @abstractmethod
    def win_msg(self, player):
        pass

    @abstractmethod
    def your_turn_msg(self, player):
        pass

    def not_move_msg(self, player):
        pass

    @abstractmethod
    def invalid_place_msg(self):
        pass

    @abstractmethod
    def get_position(self):
        pass

    @abstractmethod
    def display_score(self):
        pass

    @abstractmethod
    def display_board(self):
        pass

    @abstractmethod
    def game_mode(self):
        pass

    @abstractmethod
    def select_dif(self):
        pass