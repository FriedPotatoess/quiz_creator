#ANTI STRING INPUT
def Nostringinput(prompt):
    while True:
        user_input = input(prompt)
        
        try:
            num = float(user_input)
            return num
        except ValueError:
            print("Invalid input! Please enter a valid number.")

print("Please nput two numbers")

#Takes the input of the user
firstinput = Nostringinput("First Number: ")
secondinput = Nostringinput("Second Number: ")

#Do the operations
operationchoice = int(input("\n1:Addition\n2:Subtraction\n3:Multiplication\n4:Division\nWhat would you like to do?: "))
sum = firstinput + secondinput
difference = firstinput - secondinput
product = firstinput * secondinput
qoutient = firstinput / secondinput

if operationchoice == 1:
    print(f"the Sum of {firstinput} and {secondinput} is: {sum}")
if operationchoice == 2:
    print(f"the Difference of {firstinput} and {secondinput} is: {difference}")
if operationchoice == 3:
    print(f"the Product of {firstinput} and {secondinput} is: {product}")
if operationchoice == 4:
    print(f"the Qoutient of {firstinput} and {secondinput} is: {qoutient}")