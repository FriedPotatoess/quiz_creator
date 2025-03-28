# Create a program that ask the user to input their fullname in incorrect casing. Print the input in pascal case.

#Get the user input
user_input = input("Please input your Full name: ")

#Converts input to pascal case
pascal_case_fullname = user_input.title().replace(" ", "")

#Outputs Pascal case
print(pascal_case_fullname)