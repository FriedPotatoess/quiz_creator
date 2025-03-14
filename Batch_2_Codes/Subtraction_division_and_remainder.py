#Create a function to input to numbers √
#Create the operations needed √

print("Input two numbers")

num1 = float(input(""))
num2 = float(input(""))AS

operation = input("Choose an operation\n1:Subtraction\n2:Division\n3:Print the remainder\n:")
difference = num1 - num2
qoutient = num1 / num2
remainder = num1 % num2

if operation == '1':
    print (difference)
if operation == '2':
    print(int(qoutient))
if operation == '3':
    print (remainder)
    
