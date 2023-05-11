def find_next_empty(puzzle):
    #finds the next row, col on the puzzle that's not filled yet ---> represent -1
    #return row, col tuple (or (None, None) if there is none)
    #keep in mind that we are using 0-8 for our indices

    for r in range(9):
        for c in range(9): #range is 0,1,2...8
            if  puzzle[r][c] == -1:
                return r,c
            
    return None, None

def is_valid(puzzle, guess, row, col):
    #figures out whether the guess at the row/col of the puzzle is a valid guess
    #return true if valid

    #starting with the row
    row_values = puzzle[row]
    if guess in row_values:
        return False
    
    # #the columns
    # col_values = []
    # for i in range(9):
    #     col_values.append(puzzle[i][col])
    col_values = [puzzle[i][col] for i in range(9)]

    if guess in col_values:
        return False
    
    #and then the 3*3 square and iterate the 3 values in the row/column

    row_start = (row // 3) * 3 

    col_start = (row // 3) * 3 

    for  r in range(row_start, row_start+3):
        for c in range(col_start, col_start+3):
            if  puzzle[r][c] == guess:
                return False
            
    return True

    




def solve_sudoku(puzzle):
    #solve sudoku using backtracking
    #puzzle is a list of lists of which each list is a row in our sudoku puzzle
    #return whether a solution exists
    #mutates puzzle to be the solution if the solution exixts


    #step 1: choose somewhere on the puzzle to make a guess
    row, col = find_next_empty(puzzle)

    #step 2: if there is nowhere left, then we're done because we only allowed valid inputs

    if row is None:
        return True
    
    #step 3: if there is a place to put a number, then make a guess between 1 and 9

    for guess in range(1,10):
        #step 4 check if this is a valid guess
        if is_valid(puzzle, guess, row, col):
        #step 5 if this is valid, then place that guess on the puzzle
            puzzle[row][col] == guess
        #step 6: recursively call the function
            if solve_sudoku(puzzle):
                return True
        #step 7: if not valid or if our guess do not solve the puzzle then we need to backtrack and try new number
        puzzle[row][col] = -1 #reset the guess

        #step 8: if none of the numbers dont work! this puzzle is unresolved
        return False

if __name__ == '__main__':
    solve_sudoku()