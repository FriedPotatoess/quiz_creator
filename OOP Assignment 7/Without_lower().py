#Create a program that do the same functionality without using lower() function

def lower(user_input):
    result = ""
    for char in user_input:
        if 'A' <= char <= 'Z':
            result += chr(ord(char) + 32)
        else:
            result += char
    return result

#Gets user input
user_input = input("Please input your full name: ")


#Outputs the cleaned input
print(lower(user_input))

        
    
