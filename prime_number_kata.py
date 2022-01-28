'''
Lead Programmer: Afton Lawver
'''

# Prime Number Kata  (Coding Exercise):
# Allow the user to enter any integer 
# Display all of the prime numbers that make up  that number
# if that number is not prime already, meaning that it is only
# divisible by itself and 1.

def find_prime_numbers() -> list:
    while True:
        try:
            number = int(input('Enter any positive integer: '))
            break
        except ValueError or TypeError:
            print('Please enter a positive integer.')
    my_numbers = []
    while number > 0:
        if number % 2 == 0:
            number = number / 2
            my_numbers.append(2)
        elif number % 3 == 0:
            number = number / 3
            my_numbers.append(3)
        elif number % 5 == 0:
            number = number / 5
            my_numbers.append(5)
        elif number % 7 == 0:
            number = number / 7
            my_numbers.append(7)
        elif number == 1:
            my_numbers.append(1)
            return f'The prime numbers are {my_numbers}.'
        else:
            my_numbers.append(number)
            return f'The prime numbers are {my_numbers}.'

my_numbers = find_prime_numbers()
print(my_numbers)