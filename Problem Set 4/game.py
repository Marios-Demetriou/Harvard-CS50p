"""
In a file called game.py, implement a program that:

Prompts the user for a level,
. If the user does not input a positive integer, the program should prompt again.
Randomly generates an integer between 1 and
, inclusive, using the random module.
Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.
If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
If the guess is larger than that integer, the program should output Too large! and prompt the user again.
If the guess is the same as that integer, the program should output Just right! and exit.
"""
import random

while True:
    try:
        level = int(input("Level: "))
        # Check if Leven input is valid
        if level > 0:
            gen_guess = random.randrange(0, level)
            while True:
                try:
                    guess = int(input("Guess: "))
                    # Check if it's an int and greater than 0, then find the correct guess
                    if int(guess) and int(guess) > 0:
                        if guess < gen_guess:
                            print("Too small!")
                        elif guess > gen_guess:
                            print("Too large!")
                        else:
                            print("Just right!")
                            break
                except ValueError:
                    continue
            break
    except ValueError:
        continue
