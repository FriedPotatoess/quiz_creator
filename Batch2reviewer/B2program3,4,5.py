print("Input two numbers")

firstinp = float(input(""))
secondinp = float(input(""))

operation = input("Choose an operation\n1:Subtraction\n2:Division\n3:Print the remainder\n:")
difference = firstinp - secondinp
qoutient = firstinp / secondinp
remainder = firstinp % secondinp

if operation == '1':
    print (difference)
if operation == '2':
    print(int(qoutient))
if operation == '3':
    print (remainder)
    
