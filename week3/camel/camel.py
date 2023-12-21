# take user input
camel = input("camelCase: ").strip()
snake = ""

# Convert camelCase to snake_case
for c in camel:
    if c.upper() == c:
        snake += "_" + c.lower()
    else:
        snake += c

# print snake_case
print("snake_case:", snake)
