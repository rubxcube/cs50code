# Guessing game

import random


def guesser():

    # Reprompting user for level unless positive
    while True:
        try:
            level = int(input("Level: "))
        # Rejecting non-numeric level
        except ValueError:
            pass
        else:
            if level >= 1:
                break

    # Generating random int between 1 and level
    num = random.randint(1, level)

    while True:
        try:
            guess = int(input("Guess: "))
        # Rejecting non-numeric guess
        except ValueError:
            pass
        else:
        # Outputting response according to guess
            if guess >= 1:
                if guess == num:
                    print("Just right!")
                    break
                elif guess < num:
                    print("Too small!")
                elif guess > num:
                    print("Too large!")


guesser()
