from model.game import Game
from view.gameconsoleview import GameConsoleView
from controller.gamecontroll import GameControll

model = Game(8, 8)
view = GameConsoleView(model)
controller = GameControll(model, view)

controller.run_game()