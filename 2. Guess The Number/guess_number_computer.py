import random as random

def guess(x):
    random_number = random.randint(1, x)
    guessed_number = 0
    while guessed_number != random_number :
        guessed_number = int(input(f'Guess a number between 1 and {x}: '))

        if guessed_number < random_number:
            print("The number is too low, try again")
        elif guessed_number > random_number:
            print("The number is too high, try again")
    
    print("You have hit the guessed number")

guess(100)
