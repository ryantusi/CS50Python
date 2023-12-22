import random

# Main Function
def main():
    # Calling get_level to set the level
    level = get_level()

    # Setting total points variable
    points = 0

    # ten question start
    for _ in range(10):
        # Flag for each question answer (T|F)
        flag = False

        # Generating numbers according to the level
        x = generate_integer(level)
        y = generate_integer(level)

        # Getting the answer
        val = x + y

        # Giving three chance for the user to answer
        for _ in range(3):
            # Taking user input for answer of the question printed
            try:
                print(x, "+", y, "= ", end="")
                ans = int(input())
                if (ans == val):
                    flag = True
                    break
                else:
                    print("EEE")

            # Handling exception
            except ValueError:
                print("EEE")

        # Handling points according to the validity of the answer
        if flag == True:
            points += 1
        else:
            print(val)

    # Printing total score
    print("Score:", points)


# Function for Prompting user for level 1,2,3
def get_level():
    level = 0
    while (level < 1) or (level > 3):
        try:
            level = int(input("Level: "))
        except ValueError:
            print("Enter number between 1-3")
    return level


# Function for Creating random integer based on level
def generate_integer(level):
    x = 0
    try:
        if level == 1:
            x = random.randint(0, 9)
        elif level == 2:
            x = random.randint(10, 99)
        elif level == 3:
            x = random.randint(100, 999)
        else:
            raise ValueError
    except ValueError:
        print("Enter level (1-3)")
    return x

# Calling main function
if __name__ == "__main__":
    main()
