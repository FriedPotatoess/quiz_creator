#GOALS: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the lowest number
#Place to store the inputed numbers and the code to ask for the user to input numbers √
#Function to track the input numbers until it is invalid, then print the lowest input √

#Place to store the inputed numbers and the code to ask for the user to input numbers
#list
numbers = []

while True:
    user_input = input("Enter a number(Enter a non-number to stop): ")
        
#Function to track the input numbers until it is invalid, then print the lowest input
    try:
        num = float(user_input)
        
        if numbers.count(num) == 0:
            print("Unique")
        else:
            print ("Duplicate")
        numbers.append(num)
        
    except ValueError:
        if numbers:
            lowest_number = min(numbers)
            print(f"Program terminating. The lowest number inputted is {lowest_number}")
        else:
            print("No valid numbers were entered")
        break