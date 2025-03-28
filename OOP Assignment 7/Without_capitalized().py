#Create a program that do the same functionality without using capitalize() function.

#Definition for my own capitalize
def capitalize(user_input):
    return user_input[0].upper() + user_input[1:].lower() if user_input else user_input

#WAsk for user input
user_input = input("Enter a sentence: ")

#Output corrected input
print(capitalize(user_input))