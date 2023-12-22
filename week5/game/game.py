import random

# Prompting user for valid input
n = 0
while n <= 0:
    try:
        n = int(input("Level: "))
    except ValueError:
        print("Enter a number")

# Setting a random value
num = random.randint(1, n)

# Prompting user for guessing the number
guess = 0
while guess != num:
    try:
        guess = int(input("Guess: "))
        if guess <= 0:
            pass
        elif guess < num:
            print("Too small!")
        elif guess > num:
            print("Too large!")
        elif guess == num:
            print("just right!")
    except ValueError:
        print("Enter a number")
