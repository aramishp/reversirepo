from model.gamebase import GameBase
from view.gameview import GameView
from model.players import Players

class GameControll:
    PVAIMODE = 1
    PVPMODE = 2

    def __init__(self, model: GameBase, view: GameView) -> None:
        self.model = model
        self.view = view

    def run_game(self):
        self.view.welcome_msg()
        gamemode = self.view.game_mode()
        if gamemode == self.PVAIMODE:
            difficulty = self.view.select_dif()
        player = Players.RED_PLAYER
        counter_finish = 0
    
        #while the game is not finished, run.
        while not self.model.is_terminated():
            self.view.display_score()
            self.view.display_board()
            self.view.your_turn_msg(player) 

            #Check if a player has no moves.
            if not self.model.can_move(player):
                counter_finish += 1
                self.view.not_move_msg(player)
                #If both players has no moves, end the game.
                if counter_finish == 2:
                    break

                #Change the turn to the other player
                player = self.model.change_turn(player)
                continue  

            #Get the other player position
            if player == Players.BLACK_PLAYER and gamemode == self.PVAIMODE:  
                player_position = self.model.choose_move(difficulty)

            else:
                player_position = self.view.get_position()
                while not self.model.is_valid_move(player_position[0], player_position[1], player):
                    self.view.invalid_place_msg()
                    player_position = self.view.get_position()
        
            
            self.model.place_piece(player_position[0], player_position[1], player)
            player = self.model.change_turn(player)
            counter_finish = 0


        winner = self.model.select_winner()
        self.view.win_msg(winner)
        self.model.make_file()
        



        
