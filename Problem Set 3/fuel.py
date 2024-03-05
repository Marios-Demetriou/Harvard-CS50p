"""
Fuel gauges indicate, often with fractions, just how much fuel is in a tank.
For instance 1/4 indicates that a tank is 25% full, 1/2 indicates that a tank is 50% full,
and 3/4 indicates that a tank is 75% full.

In a file called fuel.py, implement a program that prompts the user for a fraction, formatted as X/Y,
wherein each of X and Y is an integer, and then outputs, as a percentage rounded to the nearest integer,
how much fuel is in the tank. If, though, 1% or less remains, output E instead to indicate that the
tank is essentially empty. And if 99% or more remains, output F instead to indicate that the tank is essentially full.

If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again.
(It is not necessary for Y to be 4.) Be sure to catch any exceptions like ValueError or ZeroDivisionError.
"""


def main():
    fraction = check_int("Fraction: ")


def check_int(prompt):
    while True:
        fraction = input(prompt)
        # Separate the fraction, check conditions and handle errors
        try:
            numerator, denominator = map(int, fraction.split("/"))
            if denominator == 0:
                raise ZeroDivisionError("Fraction can not have a denominator equal to zero")
            if numerator > denominator:
                raise ValueError("Numerator & Denominator must be integers|"
                                 " Numerator can not be greater than the denominator")
        except ValueError as i:
            print(i)
        except ZeroDivisionError as z:
            print(z)
        else:
            # Continue the 'try' if no exceptions found, check fuel capacity
            prompt = round(numerator / denominator * 100)
            if prompt <= 1:
                print("E")
                break

            elif 1 < prompt <= 25:
                print(f"{prompt}%")
                break

            elif 25 < prompt <= 50:
                print(f"{prompt}%")
                break

            elif 50 < prompt <= 75:
                print(f"{prompt}%")
                break

            elif 75 < prompt < 99:
                print(f"{prompt}%")
                break

            else:
                print("F")
                break


main()
