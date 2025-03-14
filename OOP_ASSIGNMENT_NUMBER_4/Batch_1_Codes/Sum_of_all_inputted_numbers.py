#Create a function that takes the input of the user
#Create a list for the numbers
#Create a function to add all the numbers

numbers = []

#Takes user input
for i in range(10):
    while True:  #Loop until a valid number is entered
        user_input = input(f"Enter number {i + 1}: ")
        
        try:
            num = float(user_input)  # Convert input to a float
            numbers.append(num)  # Add the number to the list
            break  # Exit the loop if input is valid
        except ValueError:
            print("Please input a valid number.")

#Calculate the sum of the numbers
total_sum = sum(numbers)

#Outputs sum of all the numbers
print(f"The sum of all the numbers is: {total_sum}")
