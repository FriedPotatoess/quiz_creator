#Create a function that takes the input of the user
#Create a function that decides who is larger and if the numbers are Equal

#ANTI STRING INPUT
def Nostringinput(prompt):
    while True:
        user_input = input(prompt)
        
        try:
            num = float(user_input)
            return num
        except ValueError:
            print("Invalid input! Please enter a valid number.")

print("Please input two numbers")

#Takes the input of the user
firstinput = Nostringinput("First Number: ")
secondinput = Nostringinput("Second Number: ")

#Decides who is larger
if firstinput > secondinput:
    print(f"The larger number is {firstinput}")
if secondinput > firstinput:
    print(f"The larger number is {secondinput}")
if firstinput == secondinput:
    print("Both numbers are equal")
    