#Create a program that ask the user to input a complete statement. Print the number of words in the input.

#Get the user input
user_input = input("Please input your Full name: ")
#Split the words
split_words = user_input.split()
#Output the counted splitted word
print(len(split_words))