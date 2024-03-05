"""
In a file called , reimplement Setting up my twttr from Problem Set 2, restructuring your code per the below,
wherein shorten expects a str as input and returns that same str but with all vowels (A, E, I, O, and U) omitted,
whether inputted in uppercase or lowercase.
Then, in a file called test_twttr.py, implement one or more functions that collectively test your implementation of
shorten thoroughly, each of whose names should begin with test_ so that you can execute your tests with:
pytest test_twttr.py
"""


def main():
    text = shorten(str(input("Input: ")))
    print(shorten(text))


def shorten(word):
    shortened_word = ""
    for char in word:
        if char not in "aeiouAEIOU":
            shortened_word += char
    return shortened_word


if __name__ == "__main__":
    main()
