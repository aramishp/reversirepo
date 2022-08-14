from view.boardview import BoardView

class BoardConsoleView(BoardView):

    def __init__(self, board) -> None:
        super().__init__(board)

    #Display the board in the console
    def display_board(self):
        print('  ',end='')
        for i in range(1, self.board.width+1):
            print(f'  {i} ', end='')
        print()
        header = '  ' + '-' * (4 * self.board.width + 1)
        print(header)
        for i in range(self.board.high):
            print(i+1, end=' ')
            for j in range(self.board.width):
                cell = self.board.get_cell(i, j)
                print(f'| {cell} ', end='')
            print('|')
            print(header)
        print()

    