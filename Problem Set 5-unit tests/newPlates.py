import re


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):  # Combine all functions to check if all true or not
    if len(s) < 2 or len(s) > 6:
        return False
    elif not s[:2].isalpha():
        return False
    for i in range(len(s) - 1):
        if s[i].isdigit() and s[i + 1].isalpha():
            return False
        elif s[i] == '0' and s[i - 1].isalpha():
            return False
    if bool(re.search(r"[!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~]", s)):
        return False
    return True


if __name__ == "__main__":
    main()