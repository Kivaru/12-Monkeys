import time
from player import HumanPlayer, RandomComputerPlayer, GeniusComputerPlayer

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] #we will use a single list to rep 3x3 board
        self.current_winner = None #keeping track of winner

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print__board_nums():
        # 0 | 1| 2 etc (tells what number corresponds to what box)

        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
           print('| ' + ' | '.join(row) + ' |')

    def empty_squares(self):
        return ' ' in self.board
    
    def num_empty_squares(self):
        return self.board.count(' ')
    
    def make_move(self, square, letter):

        if self.board[square] == ' ':
            self.board[square] = letter

            if self.winner(square, letter):
                self.current_winner = letter
            return True
        
        return False

    def winner(self, square, letter):

        row_index = square // 3
        row = self.board[row_index*3 : (row_index+1)*3]

        if all([spot == letter for spot in row]):
            return True
        
        col_index = square % 3
        column = [self.board[col_index+i*3] for i in range(3)]

        if(all([spot == letter for spot in column])):
            return True

        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0,4,8]] #left to right diagonal

            if all([spot == letter for spot in diagonal1]):
                return True

            diagonal2 = [self.board[i] for i in [2,4,6]] #right to left diagonal

            if all([spot == letter for spot in diagonal2]):
                return True
            
        return False


    def available_moves(self):
        #return list []
        moves = []
        return [i for i, spot in enumerate(self.board) if spot == ' ']
    
def play(game, x_player, o_player, print_game=True):
        if print_game:
            game.print__board_nums()

        letter = 'X' #starting letter
        #iterate while the game still the game has empty square
        while game.empty_squares():
            if letter == 'O':
                square = o_player.get_move(game)
            else:
                square = x_player.get_move(game)

            if game.make_move(square, letter):
                if print_game:
                    print(letter + f' makes a move to square {square}')
                    game.print_board()
                    print('')

                if game.current_winner:
                    if print_game:
                        print(letter + ' wins!')
            letter = 'O' if letter == 'X' else 'X'

            time.sleep(0.8)

        if print_game:
            print('It\'s a tie')
        
if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = GeniusComputerPlayer('O')
    t =TicTacToe()
    play(t, x_player, o_player, print_game=True)



