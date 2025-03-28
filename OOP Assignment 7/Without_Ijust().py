#Create a program that do the same functionality without using ljust() function.

#Definition that acts as Ijust,aptly named
def Ijust(user_input, width):
    if len(user_input) >= width:
        return user_input
    else:
        return user_input + ' ' * (width - len(user_input))

#Gets the input and the supposed width of the input
user_input = input("Enter what you wanna enter: ")
width = int(input("How long should it be: "))

#Prints the padded input
print(f"'{Ijust(user_input, width)}'")