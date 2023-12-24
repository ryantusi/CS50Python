# Importing libraries
import re
import sys

# Main function
def main():
    print(parse(input("HTML: ")))


def parse(s):
    # Using regex to validate the html element and url
    if match := re.search(r"^<iframe.*src=\"((http|https)://(www\.)?youtube\.com/embed/\w+).*></iframe>$", s, re.IGNORECASE):
        # Shortening the youtube link
        match_list = match.group(1).split("/")
        url = "https://youtu.be/" + match_list[len(match_list) - 1]
        return url
    else:
        # If invalid
        return None

# Calling main function
if __name__ == "__main__":
    main()
