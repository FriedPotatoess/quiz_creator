#Create a program that do the same functionality without using lstrip() function

#Definition to clean the spaces without lstring
def cleaned_input(user_input):
    i = 0
    while i < len(user_input) and user_input[i] == ' ':
        i += 1
    return user_input[i:]


#Get the user input
user_input = input("Please input your Full name: ")

#Outputs cleaned input
print(cleaned_input(user_input))