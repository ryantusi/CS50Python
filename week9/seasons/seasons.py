# importing libraries
import sys
import inflect
from datetime import date

# Initializing inflect engine
p = inflect.engine()

# main function to take input and print output
def main():
    inp = input("Date of Birth: ")
    print(convert(inp))

def convert(dob):
    # taking birth year, month, and day
    try:
        year, month, day = dob.split("-")
    except ValueError:
        sys.exit("Invalid format")
    year, month, day = int(year), int(month), int(day)

    # setting date objects
    birth = date(year, month, day)
    today = date.today()

    # sub operator overloading
    diff = today - birth

    # converting days to minutes
    days = diff.days
    min = days * 24 * 60

    # converting numbers to words
    min = p.number_to_words(min, andword="").capitalize() + " minutes"
    return min

if __name__ == "__main__":
    main()
