#Ask user to input two numbers √
#Create a function to print the numbers between the inputted numbers √

print("Input 2 numbers:")

num1 = int(input())
num2 = int(input())

if num1 <= num2:
    for num in range(num1+ 1, num2):
        print(num)