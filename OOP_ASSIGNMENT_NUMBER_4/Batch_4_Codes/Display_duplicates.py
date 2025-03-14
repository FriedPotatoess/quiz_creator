# GOALS: Create a program that ask user to input 10 numbers. Display all numbers that have duplicate.
#Place to store the inputed numbers and the code to ask for the user to input numbers √
#Create a function to track all the input numbers √
#Create a function that keep tracks of duplicate
#Create a function that prints all numbers that have duplicates √

#List
numbers = []

# Place to store the inputed numbers and the code to ask for the user to input numbers
for i in range(10):
    num = float(input(f"Enter number {i + 1}: "))
    numbers.append(num)

#Function that keep tracks of duplicate
Unique_numbers = []
Duplicates = []

for num in numbers:
    if num not in Unique_numbers:
        Unique_numbers.append(num)
    else:
        Duplicates.append(num)

#Function that prints all numbers that have duplicates
print(f"All the duplicates are: {Duplicates}")
        