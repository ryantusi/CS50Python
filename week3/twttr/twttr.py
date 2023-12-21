# take user input
text = input("Input text: ").strip()

# make a list of vowels
vowels = ["a", "e", "i", "o", "u"]

# check for vowels in text upper and lower case, remove vowels
for i in vowels:
    if (i in text):
        text = text.replace(i, "")
    if (i.upper() in text):
        text = text.replace(i.upper(), "")

# print result
print("Output:", text)
