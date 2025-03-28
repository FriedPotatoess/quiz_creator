#GOALS: Create a program that ask the user to input a number (0-1000). Print the number in 6 digit format. Add zeros at the beginning to complete the 6 digit.
#Create a fucntion to get the user input √
#Create a fucntion to make the output 6 digits 

#Get the user input
user_input = int(input("Please input your digits: "))
#Make the output 6 digits 
print(f"{user_input:06d}")