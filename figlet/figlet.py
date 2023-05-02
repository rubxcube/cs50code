# Program that makes large ASCII art letters

# Importing necessary modules
from pyfiglet import Figlet
import random
import sys


def figlet_font():

    figlet = Figlet()
    # Getting list of fonts
    fonts = figlet.getFonts()

    # Expect 0 args if user wants random font
    if len(sys.argv) == 0:
        text = input("Input: ").strip()
        figlet.setFont(font=random.choice(fonts))
        print(figlet.renderText(text))
    # Expect 3 args if user wants specific font
    elif len(sys.argv) == 3:
        # Checking argv requirements
        if (sys.argv[1] not in ["-f", "--font"]) or (sys.argv[2] not in fonts):
            sys.exit("Invalid usage")
        else:
            # Printing based on specific font
            text = input("Input: ").strip()
            figlet.setFont(font=sys.argv[2])
            print(figlet.renderText(text))
    else:
        sys.exit(1)


figlet_font()
