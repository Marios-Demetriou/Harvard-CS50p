"""
One of David’s first toys as a child, funny enough, was Little Professor, a “calculator” that would generate ten
different math problems for David to solve. For instance, if the toy were to display 4 + 0 = , David would (hopefully)
answer with 4. If the toy were to display 4 + 1 = , David would (hopefully) answer with 5. If David were to answer
incorrectly, the toy would display EEE. And after three incorrect answers for the same problem, the toy would simply
display the correct answer (e.g., 4 + 0 = 4 or 4 + 1 = 5).

In a file called professor.py, implement a program that:

Prompts the user for a level,
. If the user does not input 1, 2, or 3, the program should prompt again.
Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is a non-negative integer with
 digits. No need to support operations other than addition (+).
Prompts the user to solve each of those problems. If an answer is not correct (or not even a number), the program should
 output EEE and prompt the user again, allowing the user up to three tries in total for that problem. If the user has
 still not answered correctly after three tries, the program should output the correct answer.
The program should ultimately output the user’s score: the number of correct answers out of 10.
"""
import random


def main():
    level = get_level()
    generate_integer(level)


def get_level():
    while True:
        level = int(input("Level: "))
        if level == 1 or level == 2 or level == 3:
            return level


def generate_integer(level):
    score = 0 # Set the counter for correct answers
    for _ in range(10): # Give 10 equations with different x, y
        if level == 1:
            x = random.randint(1, 8)
            y = random.randint(1, 8)
        elif level == 2:
            x = random.randint(10, 98)
            y = random.randint(10, 98)
        elif level == 3:
            x = random.randint(100, 998)
            y = random.randint(100, 998)
        for _ in range(3):# Number of tries per equation
            try:
                answer = int(input(f"{x}+{y}= "))
            except ValueError:
                print("EEE")
                continue
            if answer == x + y:
                score += 1
                break
            else:
                print("EEE")
        print(f"{x}+{y}= ", x + y)
    print(f"Score: {score}")


if __name__ == "__main__":
    main()
