from cmath import inf
import random
import copy
from model.players import Players
from model.gamefile import Gamefile
from model.gamebase import GameBase
from model.board import Board

class Game(GameBase):
    
    def __init__(self, high, width, file_path='gamefile.txt') -> None:
        super().__init__(high, width, file_path)
        self.board = Board(self.high, self.width)

    def make_file(self):
        gamefile = Gamefile(self.file_path, self.select_winner(), self.board)
        gamefile.game_file()

    #Check if a player's location choose is valid
    def is_valid_move(self, x, y, player: Players): 
        """This function check if player can put a piece in a position
        """
    
        #Check if position in the board is available
        if self.board.get_cell(x, y) != self.board.EMPTY_CELL:
            return False
        #Check if position is out of range of the board
        if self.is_out_of_range(x, y):
            return False

        #Check every direction
        for direction in self.directions:
            current_place = (x, y)
            current_place = (current_place[0] + direction[0], current_place[1] + direction[1])
            if self.is_out_of_range(current_place[0], current_place[1]):
                continue
            if self.board.get_cell(current_place[0], current_place[1]) == player:
                continue
            #Advance in the direction
            while not self.is_out_of_range(current_place[0], current_place[1]):
                if self.board.get_cell(current_place[0], current_place[1]) == self.board.EMPTY_CELL:
                    break 
                #Change the enemy pieces
                if self.board.get_cell(current_place[0], current_place[1]) == player: 
                    return True
                #Continue advancing
                current_place = (current_place[0] + direction[0], current_place[1] + direction[1])
                
        return False

    #Make the move
    def place_piece(self, x, y, player: Players):     
        #Check every direction
        for direction in self.directions:
            current_place = (x, y)
            current_place = (current_place[0] + direction[0], current_place[1] + direction[1])
            if self.is_out_of_range(current_place[0], current_place[1]):
                continue
            if self.board.get_cell(current_place[0], current_place[1]) == player:
                continue
            #Advance in the direction
            while not self.is_out_of_range(current_place[0], current_place[1]):
                if self.board.get_cell(current_place[0], current_place[1]) == self.board.EMPTY_CELL:
                    break 
                #Change the enemy pieces
                if self.board.get_cell(current_place[0], current_place[1]) == player: 
                    while current_place != (x, y):
                        current_place = (current_place[0] - direction[0], current_place[1] - direction[1])                        
                        self.board.update_cell(current_place[0], current_place[1], player)
                    break
                #Continue advancing
                current_place = (current_place[0] + direction[0], current_place[1] + direction[1])
            
    def is_out_of_range(self, x, y):
        if x < 0 or x >= self.width or y < 0 or y >= self.high:
            return True
        return False

    def is_terminated(self):
        for i in range(self.board.high):
            for j in range(self.board.width):
                if self.board.mat[i][j] == self.board.EMPTY_CELL:
                    return False
        return True

    def change_turn(self, player: Players):
        if player == Players.BLACK_PLAYER:
            return Players.RED_PLAYER
        if player == Players.RED_PLAYER:
            return Players.BLACK_PLAYER

    def select_winner(self):
        player_red_score = self.board.score(Players.RED_PLAYER)
        player_black_score = self.board.score(Players.BLACK_PLAYER)
        if player_red_score < player_black_score:
            winner = Players.BLACK_PLAYER
        elif player_red_score > player_black_score:
            winner = Players.RED_PLAYER
        else:
            winner = Players.DRAW
        return winner
    
    def can_move(self, player: Players):
        for i in range(self.high):
                for j in range(self.width):
                    if self.is_valid_move(i, j, player):
                        return True
        return False

    #Old ai player, project part 3
    def ai_move(self, player: Players):
        better_locations = []
        high_score = self.board.score(player)
        
        holdboard = copy.deepcopy(self)
        
        moves = holdboard.valid_moves(player)
        for move in moves:
            holdboard.place_piece(move[0], move[1], player)
            new_score = holdboard.board.score(player)

            if new_score == high_score:
                better_locations.append((move[0], move[1]))

            elif new_score > high_score:
                better_locations.clear()
                better_locations.append((move[0], move[1]))
                high_score = new_score
                        
            holdboard = copy.deepcopy(self)    
        
        return random.choice(better_locations)

    def valid_moves(self, player: Players):
        moves = []
        for i in range(self.high):
            for j in range(self.width):
                if self.is_valid_move(i, j, player):
                    moves.append((i, j))
        
        return moves
        
    def minimax(self, max_player: Players, min_player: Players, difficulty):
        
        if self.is_terminated():
            max_player_score = self.board.score(max_player)
            min_player_score = self.board.score(min_player)
            if max_player_score > min_player_score:
                return 1
            if max_player_score < min_player_score:
                return -1
            if max_player_score == min_player_score:
                return 0

        elif difficulty == 0:
            max_player_score = self.board.score(max_player)
            min_player_score = self.board.score(min_player)
            
            if max_player is Players.RED_PLAYER:
                return min_player_score
            else:
                return max_player_score

        holdboard = copy.deepcopy(self)
        values = []
        moves = holdboard.valid_moves(min_player)
        
        for move in moves:
            holdboard.place_piece(move[0], move[1], min_player)
            board_value = holdboard.minimax(min_player, max_player, difficulty-1)
            values.append(board_value)
            holdboard = copy.deepcopy(self)
        
        if max_player is Players.RED_PLAYER:
                return max(values)
        else:
                return min(values)
                
    def choose_move(self, dif, player=Players.BLACK_PLAYER, oponent=Players.RED_PLAYER):
        holdboard = copy.deepcopy(self)
        moves = holdboard.valid_moves(player)
        hold = float(-inf)
        best_move = moves[0]
       
        for move in moves:
            holdboard.place_piece(move[0], move[1], player)
            board_value = holdboard.minimax(player, oponent, dif)
            
            if board_value > hold:
                hold = board_value
                best_move = move

            holdboard = copy.deepcopy(self)
        
        return best_move

            





