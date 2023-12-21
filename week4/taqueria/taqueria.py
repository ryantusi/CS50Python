# Setting menu
menu = {
    "baja taco": 4.25,
    "burrito": 7.50,
    "bowl": 8.50,
    "nachos": 11.00,
    "quesadilla": 8.50,
    "super burrito": 8.50,
    "super quesadilla": 9.50,
    "taco": 3.00,
    "tortilla salad": 8.00
}

# Initializing the variable total
total = 0.00

# Exception Handling
while True:
    # Taking user input, computing total, and printing total in format
    try:
        item = input("Item: ").lower()
        total += menu[item]
        print("Total:", "$" + format(total, ".2f"))

    # Item not in menu
    except KeyError:
        print("Enter correct item in menu")

    # Exiting the program
    except EOFError:
        break

