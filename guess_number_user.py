import random as random

def computer_guess(x):

    lowest_guess = 1
    highest_guess = x
    feedback = ''

    while feedback != 'c':
        if lowest_guess != highest_guess:
            guess_number = random.randint(lowest_guess, highest_guess)
        else:
            guess_number = lowest_guess
        feedback = input(f'Is the {guess_number} too high(H), too low (L) or correct (C)?').lower()
        if feedback == 'h':
            highest_guess = guess_number - 1
        elif feedback == 'l':
            lowest_guess = guess_number + 1

    print(f'The computer has guessed the number {guess_number}correctly!!')


