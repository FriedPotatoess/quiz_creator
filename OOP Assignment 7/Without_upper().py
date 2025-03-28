#Create a program that do the same functionality without using upper() function

def upper(user_input):
    result = ""
    for char in user_input:
        if 'a' <= char <= 'z':
            result += chr(ord(char) - 32)
        else:
            result += char
    return result

#Gets user input
user_input = input("Please input your full name: ")


#Outputs the cleaned input
print(upper(user_input))

        
    

