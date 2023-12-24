import sys

# Checking command line argument validity
if len(sys.argv) == 2:
    # Storing file name and exiting if file is not python
    arg = sys.argv[1]
    if ".py" not in arg:
        sys.exit("Not a python file")

    # declaring count variable for no. of lines
    count = 0

    # Reading lines of codes and counting code lines
    try:
        with open(arg) as file:
            lines = file.readlines()
            for line in lines:
                if line.isspace():
                    pass
                else:
                    line = line.strip()
                    if line.startswith("#"):
                        pass
                    else:
                        count += 1

    # If invalid file
    except FileNotFoundError:
        sys.exit("Enter valid file")

    # Printing number of lines
    print(count)

# Exiting program if invalid command line arguments
else:
    sys.exit("Usage: python lines.py (name or path or file)")
