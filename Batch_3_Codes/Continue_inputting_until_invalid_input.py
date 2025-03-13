#GOAL: Create a program that ask user to input a number, continue asking until the user input is invalid. Display "Unique" after input when the inputted number don't have duplicate. Display "Duplicate" after input when the inputted number have duplicate.
#Place to store the inputed numbers and the code to ask for the user to input numbers √
#Function to track the input numbers, say unique if its new and say duplicate if it has a duplicate √


#Place to store the inputed numbers and the code to ask for the user to input numbers 
#List
numbers = []


while True:
    user_input = input("Enter a number(Enter a non-number to stop): ")
        
#Function to track the input numbers, say unique if its new and say duplicate if it has a duplicate 
    try:
        num = float(user_input)
        
        if numbers.count(num) == 0:
            print("Unique")
        else:
            print ("Duplicate")
        numbers.append(num)
        
    except ValueError:
        print("Invalid input. Ending program.")
        break

