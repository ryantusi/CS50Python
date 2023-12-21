# Setting months dictionary with numeric values
months = {
    "January" : "01",
    "February" : "02",
    "March" : "03",
    "April" : "04",
    "May" : "05",
    "June" : "06",
    "July" : "07",
    "August" : "08",
    "September" : "09",
    "October" : "10",
    "November" : "11",
    "December" : "12"
}

# Reprompting mechanism
while True:
    # Taking user input and formatting
    try:
        date = input("Date: ").strip()

        # If in (mm/dd/yyyy) format
        if "/" in date:
            month, day, year = date.split("/")
            month = int(month)
            day = int(day)

            # Checking for date validity
            if (month <= 12 and month > 0) and (day <= 31 and day > 0):
                print(year, f"{month:02}", f"{day:02}", sep="-")
                break
            else:
                print("Invalid Day or Month")

        # If in another format (month dd, yyyy)
        else:
            m_d, year = date.split(",")
            month, day = m_d.split(" ")
            day = int(day)

            # Cheking for date validity
            if (day <= 31 and day > 0):
                print(year, months[month.capitalize()], f"{day:02}", sep="-")
                break
            else:
                print("Invalid Day")

    # Handling Exceptions
    except ValueError:
        print("Enter proper format (mm/dd/yyyy or month dd, yyyy)")
    except KeyError:
        print("Enter proper name of the month")

