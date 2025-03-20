#GOALS: Create a program that ask the user to input their fullname with several space characters at the beginning. Print the input without the spaces in the beginning.
#Ask for the input of the fullname √
#Figure out how to get only the useable input ex. no space √

#Asks for input
fullname = input("Please insert your full name")

#Cleans input
cleaned_fullname = fullname.lstrip()
print(cleaned_fullname)