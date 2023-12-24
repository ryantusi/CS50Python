import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    # Using regex to validate and using findall() to find the pattern of 'um'
    um_count = len(re.findall(r'\bum\b', s, re.IGNORECASE))
    return um_count

if __name__ == "__main__":
    main()
