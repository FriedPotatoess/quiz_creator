#GOALS: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number with the most number of duplicate.
#Place to store the inputed numbers and the code to ask for the user to input numbers until they put an invalid number √
#Create a function that keep tracks of duplicate √
#Create a function that prints the number with the most duplicate √

#Place to store the inputed numbers and the code to ask for the user to input numbers until they put an invalid number
#List
numbers = []
count = {}
while True:
    user_input = input("Enter a number(Enter a non-number to stop): ")
    
    try:
        num = float(user_input)
#Function that keep tracks of duplicate
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
        
    except ValueError:
        print("Invalid input, terminating program")
        break 

1
Most_duplicated = None


for num, times in count.items():
    if Most_duplicated is None or times > count[Most_duplicated]:
        Most_duplicated = num
        
#Function that prints the number with the most duplicate
if Most_duplicated is not None:
    print(f"The most duplicated number is: {Most_duplicated}")