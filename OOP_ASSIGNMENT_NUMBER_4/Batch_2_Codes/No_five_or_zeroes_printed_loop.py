#Define initial value of nu, √
#Create a while loop that prints number that does not end in 5 or 0 √

num = 0

while num <= 100:
    if num % 10 != 0 and num % 5 != 0:
        print(num)
    num += 1