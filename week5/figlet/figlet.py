# Import all Libraries
import sys
import random
from pyfiglet import Figlet

# Instantiate Figlet and store all the fonts
figlet = Figlet()
fonts = figlet.getFonts()

# If no font is specified, print in random font
if len(sys.argv) == 1:
    text = input("Input: ")
    figlet.setFont(font = random.choice(fonts))
    print("Output:", figlet.renderText(text))

# If font is specified
elif len(sys.argv) == 3:
    # Checking command line argument validity
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        # Cheking font name validity
        if sys.argv[2] not in fonts:
            sys.exit("Use existing font name")

        # Printing result
        text = input("Input: ")
        f_type = sys.argv[2]
        figlet.setFont(font = f_type)
        print("Output:", figlet.renderText(text))
    else:
        # Exiting if command line validity not satisfied
        sys.exit("Usage: python figlet.py (-f or --font) font_name")

# Exiting if command line validity not satisfied
else:
    sys.exit("Usage: python figlet.py (-f or --font) font_name")

