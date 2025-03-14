#GOAL:Create a program that ask user to input 10 numbers. Display all numbers. For numbers with duplicate, display only the first entry.
#Place to store the inputed numbers and the code to ask for the user to input 10 numbers √
numbers = []

print("Please input 10 numbers")

for i in range(10):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)

#List for numbers without duplicate and first instance of duplicate numbers
unique_numbers = []

#Function that keeps track of unique numbers √
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)
        
print(f"The exempted numbers are: {unique_numbers}")