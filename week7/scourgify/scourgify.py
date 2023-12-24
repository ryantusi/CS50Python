import sys
import csv

# Checking for command line arguments validity
if len(sys.argv) == 3:
    # Setting the input file and output file
    inp = sys.argv[1]
    out = sys.argv[2]

    # Instantiating first, last name, and house lists to store
    first = []
    last = []
    house = []

    # Reading the contents and filtering first and last name, and house
    try:
        with open(inp) as file:
            rows = csv.DictReader(file)
            for row in rows:
                l_name, f_name = row["name"].split(",")
                first.append(f_name.strip())
                last.append(l_name.strip())
                house.append(row["house"])

    # Exception handling
    except FileNotFoundError:
        sys.exit("Invalid File")

    # Writing the new and clean content into a new CSV file
    with open(out, "w") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writerow({"first": "first", "last": "last", "house": "house"})
        for i in range(len(first)):
            writer.writerow({"first": first[i], "last": last[i], "house": house[i]})

# Invalid Command Line Arguments
else:
    sys.exit("Usage: python scourgify.py input.csv output.csv")
