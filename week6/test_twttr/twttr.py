def main():
    # take user input
    text = input("Input text: ").strip()

    # calling shorten and printing result
    short = shorten(text)
    print("Output:", short)



def shorten(word):
    text = word

    # make a list of vowels
    vowels = ["a", "e", "i", "o", "u"]

    # check for vowels in text upper and lower case, remove vowels
    for i in vowels:
        if (i in text):
            text = text.replace(i, "")
        if (i.upper() in text):
            text = text.replace(i.upper(), "")

    return text


if __name__ == "__main__":
    main()
