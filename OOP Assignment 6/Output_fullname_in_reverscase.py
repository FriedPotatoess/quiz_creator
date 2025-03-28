# Create a program that ask the user to input their fullname in incorrect casing. Print each character of the input in reverse casing.

#Get the user input
user_input = input("Please input your Full name: ")
#Output reversed case
print(user_input.swapcase())