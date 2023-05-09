import math
import random

class Player:
    def __init__(self, letter):
        #letter is x or o

        self.letter = letter

        #players should get their next moves

    def get_move(self, game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        sqauare = random.choice(game.available_moves())
        return sqauare

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square  = False
        val = None

        while not valid_square:
            square = input(self.letter + '\s turn. Input move (0-8):')
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True

            except :
                print('Invalid Square. Try Again')

        return val