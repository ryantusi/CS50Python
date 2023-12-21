# take user input and make it lower without whitespaces
greet = input("Greeting: ")
greet = greet.lower().strip()

# Use conditional statement to print amount
if ("hello" in greet):
    print("$0")
elif (greet[0] == "h"):
    print("$20")
else:
    print("$100")
