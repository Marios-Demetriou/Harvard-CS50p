


def main():
    text = str(input("Greeting: ").lower())
    print(value(text))

def value(greeting):
    first_letter = greeting[0]
    if greeting == "hello" or greeting == "Hello":
        return f"$0"
    elif first_letter == "h" or first_letter == "H":
        return f"$20"
    else:
        return f"$100"


if __name__ == "__main__":
    main()