#Create a program that do the same functionality without using removeprefix() function.

#Definition to remove prefix
def remove_prefix(user_input, prefix):
    if user_input[:len(prefix)] == prefix:
        return user_input[len(prefix):]
    return user_input

#Gets the input and the prefix that is wished to be removed
user_input = input("Input your stuff: ")
prefix = input("Input which prefix you wanna remove: ")

#Outputs the input without the prefix
print(remove_prefix(user_input, prefix))