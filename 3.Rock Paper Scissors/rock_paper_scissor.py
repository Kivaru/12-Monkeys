import random as random

def game():

    user = input("Select 'r' for Rock, 'p' for Paper, and 's' for Scissor: ").lower()

    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        print('It is a tie')
    
    if is_win(user, computer):
        print('You Win')
    else:
        print('You Lost')
    

def is_win(player, opponent):

    if(player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
    
game()
    