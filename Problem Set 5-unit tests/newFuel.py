def main():
    while True:  # Keep asking for input until correct format
        fraction = input("Fraction: ")
        try:
            percentage = convert(fraction)  # Return percentage for gauge() usage
            print(gauge(percentage))
            break  # Break out of loop if conversion has succeeded
        except ValueError as e:
            print(e)
        except ZeroDivisionError as z:
            print(z)


def convert(fraction):
    # Split input into a numerator, denominator
    numerator_str, denominator_str = fraction.split("/")
    try:
        numerator = int(numerator_str)
        denominator = int(denominator_str)
    except ValueError:
        raise ValueError("Input must be in the format X/Y where X and Y are integers")
    if denominator == 0:
        raise ZeroDivisionError("Fraction can not have a denominator equal to zero")
    if numerator > denominator:
        raise ValueError(" Numerator can not be greater than the denominator")
    return round(numerator / denominator * 100)


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif 99 <= percentage <= 100:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
