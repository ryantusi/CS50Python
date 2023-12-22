# Importing emoji module
import emoji

# Taking user input
text = input("Input: ").strip()

# Printing the emojized text
print("Output:", emoji.emojize(text, language="alias"))
