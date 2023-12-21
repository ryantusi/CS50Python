# Initializing an empty dictionary
grocery = {}

# Reprompting Mechanism
while True:
    # Taking input and adding item to grocery dictionary with number of items
    try:
        item = input().upper()
        if item in grocery.keys():
            grocery[item] += 1
        else:
            grocery[item] = 1

    # Exiting the program by printing out the sorted list
    except EOFError:
        print("", end="\n\n")
        for key in sorted(grocery.keys()):
            print(grocery[key], key)
        break
