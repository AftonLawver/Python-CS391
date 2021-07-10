import functools
import operator

def difference_between_sum_of_squares(number:int):
    total = 0

    # calculation for the sum of squares 
    # sum of squares
    numbers_list = list(range(1, number + 1))
    numbers_list_final = [number ** 2 for number in numbers_list]
    
    # instead of sum, use reduce with operator.add to add all elements up. 
    sum_of_squares = functools.reduce(operator.add, numbers_list_final)
    print(sum_of_squares)
    # number_squared = number * number
    # sum_of_squares = sum_of_squares + number_squared

    # square of the sum 

    sum_of_all_numbers = functools.reduce(operator.add, numbers_list)
    square_of_sum = sum_of_all_numbers**2
    
    
    total = str(square_of_sum - sum_of_squares)
    print("The difference is: " + total)
 
difference_between_sum_of_squares(10)
