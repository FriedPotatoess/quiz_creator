# GOALS: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number from lowest to highest. Clue: sort() function
#Place to store the inputed numbers and the code to ask for the user to input numbers √
#Function to track the input numbers until it is invalid, then assort the numbers from lowest to highest √

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

#Assort the numbers from lowest to highest
    except ValueError:
        print("Invalid input. Program now ending")
        numbers.sort()
        print(f"Numbers from lowest to highest: {numbers}")
        break

