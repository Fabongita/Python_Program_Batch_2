"Prog07: Create a program that ask user to input 10 numbers. Print how many are even numbers."
def even(numbers):
    return(sum(1 for i in numbers if i % 2 == 0))
numbers =[int(input("input number"+str(i+1)+":"))for i in range(10)]
print("the number of even numbers are", even(numbers))
           
