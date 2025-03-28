#Create a program that do the same functionality without using title() function.

#Definition for my custom title
def title(user_input):
    words = user_input.split()
    capitalized_first_letter = [word[0].upper() + word[1:].lower() if word else '' for word in words]
    
    return ' '.join(capitalized_first_letter)

#Gets the user input
user_input = input("Enter a sentece: ")

#Output
print(title(user_input))