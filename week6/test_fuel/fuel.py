def main():
    # Taking input, converting to int, then to percentage or gauge meter
    fuel = input("Fuel: ").strip()
    percen = convert(fuel)
    meter = gauge(percen)
    print(meter)


def convert(fraction):
            # Spliting the fraction to get the numerator and denominator
            exp = fraction.split("/")

            # Checking value error
            x = int(exp[0])
            y = int(exp[1])

            # Checking Zero Divison error
            x/y

            # Handling logical error and returning the proper fraction if input satisfied
            if (x > y):
                raise ValueError

            # Converting it to percentage value
            perc = round((x/y) * 100)
            return perc


def gauge(percentage):
    # Returning result based on conditions
    perc = percentage
    if perc <= 1:
        return "E"
    elif perc >= 99:
        return "F"
    else:
        perc = str(perc) + "%"
        return perc


if __name__ == "__main__":
    main()
