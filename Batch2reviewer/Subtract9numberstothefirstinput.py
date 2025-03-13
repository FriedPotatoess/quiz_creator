#Create a list √
#Create the function to subtract all subsequent number after the first input √

numbers = []

for i in range(10):
    num = float(input(f"Enter number {i + 1}: "))
    numbers.append(num)

difference = numbers[0]

for num in numbers[1:]:
    difference -= num
    
print(difference)
    