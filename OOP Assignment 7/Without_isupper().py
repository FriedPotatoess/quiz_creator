#Create a program that do the same functionality without using isupper() function.
def isupper(user_input):
    for char in user_input:
        if 'a' <= char <= 'z':
            return False
    return True
#Gets the input of the user
user_input = input("PLEASE ENTER UPPERCASE ONLY, IF U ENTER LOWERCASE U WILL EXPLODE: ")

#Output, check if the input is upper only or no
if isupper(user_input):
    print("EVERYTHING IS UPPERCASE")
else:
    print("BOOM, YA DEAD")