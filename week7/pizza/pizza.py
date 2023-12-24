# Importing libraries
import csv
import sys
from tabulate import tabulate

# Checking command line validity
if len(sys.argv) == 2:
    # Checking for CSV file
    arg = sys.argv[1]
    if ".csv" not in arg:
        sys.exit("Not a CSV file")

    # Declaring headers for tables of different files
    headers_s = ["Sicilian Pizza", "Small", "Large"]
    headers_r = ["Regular Pizza", "Small", "Large"]

    # Initializing table contents
    table = []

    # Reading files
    try:
        # For sicilian file
        if arg == "sicilian.csv":
            with open(arg) as file:
                rows = csv.DictReader(file)
                for row in rows:
                    arr = [row["Sicilian Pizza"], row["Small"], row["Large"]]
                    table.append(arr)
            print(tabulate(table, headers_s, tablefmt="grid"))

        # For regular file
        elif arg == "regular.csv":
            with open(arg) as file:
                rows = csv.DictReader(file)
                for row in rows:
                    arr = [row["Regular Pizza"], row["Small"], row["Large"]]
                    table.append(arr)
            print(tabulate(table, headers_r, tablefmt="grid"))

        # if none of those both, exit
        else:
            sys.exit("Enter valid pizza files")

    # if not file exists
    except FileNotFoundError:
        sys.exit("Invalid file")

# Invalid command line arguments
else:
    sys.exit("Usage: python pizza.py (name of csv file)")
