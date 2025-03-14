#GOAL: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the highest number
#Place to store the inputed numbers and the code to ask for the user to input numbers until they put an invalid number √
#Create a function that prints the highest number

#Lists
numbers = []
highest_number = None

#Place to store the inputed numbers and the code to ask for the user to input numbers until they put an invalid number √
while True:
    user_input = input("Enter a number(Enter a non-number to stop): ")
    
    try:
        num = float(user_input)
        if highest_number is None or user_input > highest_number:
            highest_number = user_input
    except ValueError:
        print("Invalid input, terminating program")
        break
    

#Prints the highest number √
print(f"The highest number is: {highest_number}")   
