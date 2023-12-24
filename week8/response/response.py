# importing library
from validator_collection import checkers

def main():
    # taking user input
    print(is_valid(input("What's your email address? ")))

def is_valid(s):
    # using is_email function to check validity
    if checkers.is_email(s):
        return "Valid"
    else:
        return "Invalid"

if __name__ == "__main__":
    main()
