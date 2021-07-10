def difference_between_sum_of_squares(number:int):
    total = 0

    # calculation for the sum of squares 
    # sum of squares
    numbers_list = list(range(1, number + 1))
    numbers_squared = map(lambda x: x*x, numbers_list)
    list_of_squares = list(numbers_squared)
    
    sum_of_squares = sum(list_of_squares)
    print(sum_of_squares)
    # number_squared = number * number
    # sum_of_squares = sum_of_squares + number_squared

    # square of the sum 
    sum_of_all_numbers = sum(numbers_list)
    square_of_sum = sum_of_all_numbers**2
    
    total = str(square_of_sum - sum_of_squares)
    print("The difference is: " + total)
 
difference_between_sum_of_squares(10)
