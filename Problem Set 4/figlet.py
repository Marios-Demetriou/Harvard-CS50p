"""
In a file called figlet.py, implement a program that:

Expects zero or two command-line arguments:
Zero if the user would like to output text in a random font.
Two if the user would like to output text in a specific font, in which case the first of the two should be -f or --font,
 and the second of the two should be the name of the font.
Prompts the user for a str of text.
Outputs that text in the desired font.
If the user provides two command-line arguments and the first is not -f or --font or the second is not the name of a
font, the program should exit via sys.exit with an error message.
"""
import random
import sys
from pyfiglet import Figlet

f = Figlet()
fonts = f.getFonts()
if len(sys.argv) == 1:
    text = str(input("Input: "))
    random_font_name = random.choice(fonts)
    random_font = Figlet(font=random_font_name)
    print(random_font.renderText(text))
elif len(sys.argv) <=3:
    if sys.argv[1] != "-f" and sys.argv[1] != "--font":
        sys.exit("Invalid Usage")
    elif  sys.argv[2] not in fonts:
        sys.exit("Invalid Usage")
    else:
        text = str(input("Input: "))
        font = Figlet(font=sys.argv[2])
        print(font.renderText(text))
