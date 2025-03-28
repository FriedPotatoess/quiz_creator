#Create a program that do the same functionality without using center() function.

#Definition for custom center function
def center(user_input, width):
    # Calculate how many spaces to add
    total_padding = width - len(user_input)

    if total_padding <= 0:
        return user_input  

    left_padding = total_padding // 2
    right_padding = total_padding - left_padding

    return ' ' * left_padding + user_input + ' ' * right_padding

# Get user input and the width
user_input = input("Please enter what you wanna enter: ")
width = int(input("Enter the width, which i will center the text you put: "))

#Outputs the centered text
print(f"'{custom_center(user_input, width)}'")
