#GOAL:Create a program that ask user to input 10 numbers. Display all numbers that don't have duplicate.
#Place to store the inputed numbers and the code to ask for the user to input 10 numbers √
#Function that takes a list that tracks non duplicates

num = []

print("Please input 10 numbers")

for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)