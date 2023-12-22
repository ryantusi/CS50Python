def main():
    # take user input and make it lower without whitespaces
    greet = input("Greeting: ").strip()
    val = value(greet)

    # printing value in dollars
    print("$" + str(val))

def value(greeting):
    greeting = greeting.lower()
    # Use conditional statement to return value
    if ("hello" in greeting):
        return 0
    elif (greeting[0] == "h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
