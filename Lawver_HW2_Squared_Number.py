def squared_number(number:int):
    new_number_string = ""
    my_number = str(number)
    for i in my_number:
        int_number = int(i)
        int_number_squared = str(int_number * int_number)
        new_number_string = new_number_string + int_number_squared
        
    new_number_int = int(new_number_string)
    return new_number_int


