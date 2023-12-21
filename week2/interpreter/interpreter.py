# take expression from user
ex = input("Expression: ").strip()

# Split numbers and operator
x, y, z = ex.split(" ")

# Use conditional statement to compute result
match y:
    case "+":
        n = float(x) + float(z)
        n = round(n, 1)
        print(n)
    case "-":
        n = float(x) - float(z)
        n = round(n, 1)
        print(n)
    case "/":
        n = float(x) / float(z)
        n = round(n, 1)
        print(n)
    case "*":
        n = float(x) * float(z)
        n = round(n, 1)
        print(n)
    case _:
        print("unknown")
