from abc import ABC, abstractmethod

class GameBase(ABC):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, 1), (1, 1), (1, -1), (-1,-1)]

    def __init__(self, high, width, file_path='gamefile.txt') -> None:
        super().__init__()
        self.high = high
        self.width = width
        self.file_path = file_path

    @abstractmethod
    def make_file(self):
        pass
    
    @abstractmethod
    def is_valid_move(self): 
        pass

    @abstractmethod    
    def place_piece(self):     
        pass

    @abstractmethod
    def is_out_of_range(self):
        pass

    @abstractmethod
    def is_terminated(self):
        pass

    @abstractmethod
    def change_turn(self):
        pass

    @abstractmethod
    def select_winner(self):
        pass

    @abstractmethod
    def can_move(self):
        pass

    @abstractmethod
    def ai_move(self):
        pass

    @abstractmethod
    def choose_move(self):
        pass

    @abstractmethod
    def minimax(self):
        pass

    @abstractmethod
    def valid_moves(self):
        pass