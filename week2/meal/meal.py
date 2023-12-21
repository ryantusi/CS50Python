def main():
    # Taking user inputer time and coverting it to float
    time = convert(input("Time: ").strip())

    # Analyzing time and printing
    if (time >= 7 and time <= 8):
        print("breakfast time")
    elif (time >= 12 and time <= 13):
        print("lunch time")
    elif (time >= 18 and time <= 19):
        print("dinner time")

def convert(time):
    # Converting 24-hour time format to float
    x, y = time.split(":")
    x = float(x)
    y = float(y)
    y /= 60
    return x + y

# Calling main function
if __name__ == "__main__":
    main()
