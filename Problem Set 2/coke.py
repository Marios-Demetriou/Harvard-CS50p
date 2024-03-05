"""
Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents and only accepts coins in these denominations:
25 cents, 10 cents, and 5 cents.

In a file called coke.py, implement a program that prompts the user to insert a coin, one at a time,
each time informing the user of the amount due.
Once the user has inputted at least 50 cents, output how many cents in change the user is owed.
Assume that the user will only input integers, and ignore any integer that isn’t an accepted denomination.
"""


def main():
    check_denomination()


def check_denomination():
    coke = 50
    while coke > 0:
        print(f"Amount Due:{coke}")
        coin = int(input("Insert Coin: "))
        if coin == 25 or coin == 10 or coin == 5:
            coke = coke - coin
        elif coke == 0:
            break
        continue
    print(f"Change Owed: {coke}")


main()
