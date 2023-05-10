#create board class and its properties
import random
import re
class Board:
    def __init__(self, dim_size, num_bombs):
        self.dim_size = dim_size
        self.num_bombs = num_bombs

        #creating the board
        #using helper function
        self.board = self.make_new_board() #plant the bombs
        self.assigned_values_to_board()


        #initialize a set to keep track of uncovered locations and set them as tuples (row,col)
        self.dug = set() #if we dig at 0,0 then self.dug = {(0,0)}

    def make_new_board(self):
        #make a board according to dim_size and num_bombs
        #generate a new board

        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        #this creates something like this
        #[[None, None, ..., None],
        # [None, None, ..., None]
        # [None, None, ..., None]
        # ...
        # [None, None, ..., None]]

        #plant the bomb
        bombs_planted = 0

        while bombs_planted < self.num_bombs:
            location = random.randint(0, self.dim_size**2 - 1)
            row = location // self.dim_size
            col = location % self.dim_size

            if board[row][col] == '*':
                #this means the bomb has been already planted so keep going
                continue
            board[row][col] = '*'
            bombs_planted += 1

        return board
    
    def assigned_values_to_board(self):
        #assign 0-8 for all empty spaces

        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.board[r][c] == '*':
                    #if this is a bomb, no need to calcualte anything
                    continue
                self.board[r][c] = self.get_num_neighbouring_bombs(r,c)

    def get_num_neighbouring_bombs(self, row, col):
        #iterate through each of the neighbouring positions and sum number of bombs
        num_neighbouring_bombs = 0

        for r in range(max(0,row-1), min(self.dim_size-1, row+1) + 1):
            for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1):
                if r == row and c == col:
                    #original location, do nothing
                    continue
                if self.board[r][c] == '*':
                    num_neighbouring_bombs += 1

        return num_neighbouring_bombs

    def dig(self, row, col):
        #dig at  that location, return true if successful dig false if bomb dug
        self.dug.add((row, col)) #keeping track we dug here

        if self.board[row][col] == '*':
            return False
        
        elif self.board[row][col] > 0:
            return True
        
        for r in range(max(0,row-1), min(self.dim_size-1, row+1) + 1):
            for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1):
                if (r,c) in self.dug:
                    continue
                self.dig(r,c)

        return True
    

    def __str__(self):
        # this is a magic function where if you call print on this object,
        # it'll print out what this function returns!
        # return a string that shows the board to the player

        # first let's create a new array that represents what the user would see
        visible_board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if (row,col) in self.dug:
                    visible_board[row][col] = str(self.board[row][col])
                else:
                    visible_board[row][col] = ' '
        
        # put this together in a string
        string_rep = ''
        # get max column widths for printing
        widths = []
        for idx in range(self.dim_size):
            columns = map(lambda x: x[idx], visible_board)
            widths.append(
                len(
                    max(columns, key = len)
                )
            )

        # print the csv strings
        indices = [i for i in range(self.dim_size)]
        indices_row = '   '
        cells = []
        for idx, col in enumerate(indices):
            format = '%-' + str(widths[idx]) + "s"
            cells.append(format % (col))
        indices_row += '  '.join(cells)
        indices_row += '  \n'
        
        for i in range(len(visible_board)):
            row = visible_board[i]
            string_rep += f'{i} |'
            cells = []
            for idx, col in enumerate(row):
                format = '%-' + str(widths[idx]) + "s"
                cells.append(format % (col))
            string_rep += ' |'.join(cells)
            string_rep += ' |\n'

        str_len = int(len(string_rep) / self.dim_size)
        string_rep = indices_row + '-'*str_len + '\n' + string_rep + '-'*str_len

        return string_rep
        






def play(dim_size = 10, num_bombs=10):
    #1.create the board and plant the bombs

    board =  Board(dim_size, num_bombs)

    safe = True

    #2.show the user the board and ask them where they want to dig
    #3.if location is a bomb, show game over message, 
    # if the location is not the bomb dig recursively until each square
    #is at least next to a bomb 
    #4.repeat step 2 and 3 until there are no more places to dig->VICTORY
    while len(board.dug) < board.dim_size**2 - num_bombs:
        print(board)
        user_input = re.split(',(\\s)*', input("Where would you like to dig? Input as row, col: "))
        row, col = int(user_input[0]), int(user_input[-1])

        if row < 0 or row >= board.dim_size or col < 0 or col >= dim_size:
            print("Invalid Location, Try again")
            continue
        safe = board.dig(row, col)

        if not safe:
            break #game over

    if safe:
        print("Victory")
    else:
        print("Game Over")
        #show the whole board
        board.dug = [(r,c) for r in range(board.dim_size) for c in range(board.dim_size)]
        print(board)

if __name__ == '__main__':
    play()