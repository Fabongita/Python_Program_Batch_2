"Prog06: Create a program that ask user to input 10 numbers. Print the result of the first number minus all of the remaining numbers."
numbers = [int(input("input number "+str(i+1)+":"))for i in range(10)]
x = 0
for i in numbers[1:]:
    y = numbers[0]-numbers[1]
    x = y
print(x)
            
