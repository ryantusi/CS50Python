# Main Function
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # Converts $##.## to ##.#
    num = d
    num = num.replace("$", "")
    num = round(float(num), 1)
    return num


def percent_to_float(p):
    # Converts ##% to 0.##
    num = p
    num = num.replace("%", "")
    num = round(float(num)/100, 2)
    return num

main()
