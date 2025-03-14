#GOALS: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the average.
#Place to store the inputed numbers and the code to ask for the user to input numbers until they put an invalid number
#Function to track the input numbers until it is invalid, then get the average of all the numbers

#List
numbers = []

#Place to store the inputed numbers and the code to ask for the user to input numbers until they put an invalid number
while True:
    user_input = input("Enter a number(Enter a non-number to stop): ")
    
    try:
        num = float(user_input)
        numbers.append(numbers)
    except ValueError:
        print("Invalid input, terminating program")
        break