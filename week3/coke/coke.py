# set coke bottle price
coke = 50

# Use loop to prompt user to insert coins till amount due is cleared
while coke > 0:
    print("Amount Due:", coke)
    n = int(input("Insert coin: "))
    if n == 25:
        coke -= 25
    elif n == 10:
        coke -= 10
    elif n == 5:
        coke -= 5
    else:
        continue

# Compute change owed
if coke < 0:
    print("Change Owed:", -1 * (coke))
else:
    print("Change Owed:", coke)
