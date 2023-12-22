# Importing library
import inflect

# Instantiating inflect engine
inflct = inflect.engine()

# Setting names list
names = []

# Reprompting mechanism
while True:
    # Taking user input for names and appending to the names list
    try:
        name = input("Name: ")
        names.append(name)

    # Exiting the program and printing the result
    except EOFError:
        print("", end="\n\n")
        print("Adieu, adieu, to " + inflct.join(names))
        break
