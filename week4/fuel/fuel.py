# Main Function
def main():
    # Take fuel input by calling get_fuel()
    fuel = get_fuel("Fraction: ")

    # Convert fuel fraction to percentage by calling convert_to_perc()
    converted = convert_to_perc(fuel)

    # Print result
    print(converted)


def convert_to_perc(arr):
    # Converting it to percentage value
    perc = round((arr[0]/arr[1]) * 100)

    # Returning result based on conditions
    if perc <= 1:
        return "E"
    elif perc >= 99:
        return "F"
    else:
        perc = str(perc) + "%"
        return perc


def get_fuel(prompt):
    # Reprompting mechanism
    while True:
        try:
            # taking input from user
            exp = input(prompt)

            # Spliting the fraction to get the numerator and denominator
            exp = exp.split("/")

            # Checking value error
            x = int(exp[0])
            y = int(exp[1])

            # Checking Zero Divison error
            x/y

            # Handling logical error and returning the proper fraction if input satisfied
            if (x > y):
                print("Input Error in fraction (x/y): x > y")
            else:
                return [x, y]

        # Catching Exceptions
        except ValueError:
            print("Input in proper fraction (x/y)")
        except ZeroDivisionError:
            print("Input (x/y) where y > 0")


# Calling main function
main()
