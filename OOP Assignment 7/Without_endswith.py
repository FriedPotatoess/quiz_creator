#Create a program that do the same functionality without using endswith() function.

#Custom endswith
def endswith(user_input, suffix):
    return user_input[-len(suffix):] == suffix

#Gets the input and the suffix
user_input = input("Please enter ya stuff: ")
suffix = input("Please enter the suffix you want to check: ")

if endswith(user_input, suffix):
    print(f"The string ends with {suffix}")
else:
    print(f"The string does not end with {suffix}")