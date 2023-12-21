# main function
def main():
    # Take user input
    string = input("Enter: ")

    # call convert()
    converted = convert(string)

    # print result
    print(converted)

def convert(str):
    # Replacing emoticons with emojis
    new = str
    new = new.replace(":)", "🙂")
    new = new.replace(":(", "🙁")
    return new

# calling main()
main()
