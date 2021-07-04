def difference_between_sum_of_squares(number:int):
    sum_of_squares = 0
    square_of_sums = 0
    sum = 0

    # calculation for the sum of squares 
    while number > 0:
        # sum of squares
        number_squared = number * number
        sum_of_squares = sum_of_squares + number_squared
        

        # square of the sum 
        sum = sum + number
        sum_squared = sum * sum
        number -= 1

    total = str(sum_squared - sum_of_squares)
    print("The difference is: " + total)


difference_between_sum_of_squares(20)
