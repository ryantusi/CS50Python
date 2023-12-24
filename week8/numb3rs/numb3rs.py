# importing functions
import re
import sys

# main function
def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    # Using regex to check for pattern: #.#.#.# where '#' <= 255
    if re.search(r"^([0-2]?[0-5]?[0-5]|[0-2]?[0-4]?[0-9])\.([0-2]?[0-5]?[0-5]|[0-2]?[0-4]?[0-9])\.([0-2]?[0-5]?[0-5]|[0-2]?[0-4]?[0-9])\.([0-2]?[0-5]?[0-5]|[0-2]?[0-4]?[0-9])$", ip):
        return True
    else:
        return False

# calling main function
if __name__ == "__main__":
    main()
