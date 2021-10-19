

'''
# using a for loop to print out the decimal equivalents of 1/2, 
# 1/3, 1/4, 1/5, 1/6, 1/7, 1/8, 1/9, 1/10. f

for i in range(2,11):
    value = float(1/i)
    print("1/{}: {}".format(i, value))
    '''

'''
# using a while loop that asks the user for a number, and prints a countdown
# from that number to zero. Make sure your program can handle negative nums. 

while True:
    num = int(input("Enter a number: "))
    string_num = str(num)
    if string_num[0] == "-":
        print("Please enter a positive integer.")
        continue
    else:
        break

while num >= 0:
    print(num)
    num -= 1

'''

'''
# write a program with a for loop that calculates exponentials. 
# Ask the user for a base and an exponent. 

base = int(input("Enter a base: "))
exponent = int(input("Enter an exponent: "))
print(base**exponent)

'''

while True:
    number = int(input("Enter a number that is divisible by 2: "))
    if number % 2 == 0:
        print("Finally, you entered a number divisible by 2. Took long enough!")
        break
    else: 
        print("Nice try. Think harder.")
        continue


