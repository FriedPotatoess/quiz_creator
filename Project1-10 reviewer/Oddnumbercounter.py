#Create a function that takes the input of the user
#Create a list for the numbers
#Create a function to output how many odd numbers are inputted


numbers = []

# Takes user input
for i in range(10):
    while True:  
        user_input = input(f"Enter number {i + 1}: ")

        # Anti float input
        try:
            num = int(user_input)
            numbers.append(num)
            break  # Exit the loop if the input is valid
        except ValueError:
            print("Please input an integer")

# Counts the odd numbers
odd_count = sum(1 for num in numbers if num % 2 != 0)

# Output the odd numbers
print(f"There are {odd_count} odd numbers in the numbers that you inputted.")
