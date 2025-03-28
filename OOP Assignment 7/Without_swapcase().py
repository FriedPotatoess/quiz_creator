#Create a program that do the same functionality without using swapcase() function.

#Definition for custom swapcase function
def swapcase(user_input):
    swapped_string = ""
    for char in user_input:
        if char.islower():
            swapped_string += char.upper()  
        elif char.isupper():
            swapped_string += char.lower()  
        else:
            swapped_string += char  
    return swapped_string

# Get user input
user_input = input("Enter what texted you want case swapped: ")

#Outputs swapcased
print(f"'{swapcase(user_input)}'")
