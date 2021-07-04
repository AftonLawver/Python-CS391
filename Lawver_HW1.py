def book(my_list:list):
    length = len(my_list)
    if length == 0:
        print("no one has read this")            
        
    elif length == 1:
        print(my_list[0] + " has read this")

    elif length == 2:
        print(my_list[0] + " and " + my_list[1] + " have read this")

    elif length == 3:
        print(my_list[0] + ", " + my_list[1] + " and " + my_list[2] + " have read this")

    else: 
        first_two_readers = my_list[0] + ", " + my_list[1] + " and "
        new_length = str(length - 2)
        print(first_two_readers + new_length + " others have read this")


book(['Afton', 'Piotr', 'Alliyah', 'Nolan','Afton', 'Piotr', 'Alliyah', 'Nolan'])
        