"""
In Massachusetts, home to Harvard University, it’s possible to request a vanity license plate for your car,
with your choice of letters and numbers instead of random ones. Among the requirements, though, are:

“All vanity plates must start with at least two letters.”
“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
“Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable
… vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
“No periods, spaces, or punctuation marks are allowed.”
In plates.py, implement a program that prompts the user for a vanity plate and then output Valid
if meets all of the requirements or Invalid if it does not. Assume that any letters in the user’s input will be
uppercase. Structure your program per the below, wherein is_valid returns True if s meets all requirements
and False if it does not. Assume that s will be a str. You’re welcome to implement additional functions for is_valid
to call (e.g., one function per requirement).
"""

import re

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s) :
    if begin_char(s) is True and max_char(s) is True and in_middle(s) is True and zero_char(s) is True and special_char(s) is True:
        return True


def begin_char(begin):
    if begin[:2].isalpha():
        return True
    else:
        return False


def max_char(max):
    if 2 <= len(max) <= 6:
        return True
    else:
        return False


# Iterate over index to check if numbers in the middle
def in_middle(string_name):
    # Ensure loop does not go out of range(am checking i+1)
    for i in range(len(string_name) - 1):
        if string_name[i].isdigit() and string_name[i + 1].isalpha():
            return False

    return True


def zero_char(zero):
    # Ensure loop does not go out of range(am checking i+1)
    for i in range(len(zero) - 1):
        if zero[i] == '0' and zero[i - 1].isalpha():
            return False
    return True


def special_char(sp):
    if bool(re.search(r"[!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~]", sp)):
        return False
    else:
        return True

main()
