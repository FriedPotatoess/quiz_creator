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
firstinput = Nostringinput("Base: ")
secondinput =Nostringinput("Exponent: ")

#Do the operation
result = firstinput ** secondinput

print(f"The result of {firstinput} raised to {secondinput} is {result}")