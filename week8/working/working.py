# Importing Libraries
import re
import sys

# Creating a dictionary 12-24 hour format
times = {
"12AM":	"00",
"1AM":	"01",
"2AM":	"02",
"3AM":	"03",
"4AM":	"04",
"5AM":	"05",
"6AM":	"06",
"7AM":	"07",
"8AM":	"08",
"9AM":	"09",
"10AM":	"10",
"11AM":	"11",
"12PM":	"12",
"1PM":	"13",
"2PM":	"14",
"3PM":	"15",
"4PM":	"16",
"5PM":	"17",
"6PM":	"18",
"7PM":	"19",
"8PM":	"20",
"9PM":	"21",
"10PM":	"22",
"11PM":	"23",
"12AM":	"00"
}

# main function
def main():
    print(convert(input("Hours: ")))


def convert(s):
    # Using regex to check validity of 12 hour format: '##:##|## AM|PM to ##:##|## AM|PM'
    if matches := re.search(r"^((12|[1-9]?|[1][0-2]?):?([0-5]?[0-9]?) (AM|PM)) to ((12|[1-9]?|[1][0-2]?):?([0-5]?[0-9]?) (AM|PM))$", s, re.IGNORECASE):
        # If 12 hour format in '## AM|PM to ## AM|PM' and converting to 24 hour format
        if matches.group(3) == "" or matches.group(7) == "":
            converted = times[matches.group(2) + matches.group(4)] + ":00" + " to " + times[matches.group(6) + matches.group(8)] + ":00"

        # If 12 hour format in '##:## AM|PM to ##:## AM|PM' and converting to 24 hour format
        else:
            converted = times[matches.group(2) + matches.group(4)] + ":" + matches.group(3) + " to " + times[matches.group(6) + matches.group(8)] + ":" + matches.group(7)

        return converted

    # If not valid format
    else:
        raise ValueError


if __name__ == "__main__":
    main()
