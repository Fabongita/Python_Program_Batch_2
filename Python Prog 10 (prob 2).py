"Prog10: Create a program that ask user to input 2 numbers. Print all the numbers between the two numbers."
def between(x, y):
    if x < y:
        return range(x + 1, y)
    else:
        return range(y + 1, x)

x = int(input("Input the first number: "))
y = int(input("Input the second number: "))

print(f"The numbers between {x} and {y} are: {list(between(x, y))}")
