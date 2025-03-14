#Create a for loop to output numbers 1-100 with the exception of numbers that end in 0



for num in range(1, 101):
    if num % 10 != 0:
        print(num)
