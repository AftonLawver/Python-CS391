# Given an integer, return the integer with reversed digits.
# Note: The integer could be either positive or negative.

def reverse_integer(n:int):
    string = str(n)

    if string[0] == "-":
        return int("-" + string[::-1])
    
    else:
        return int(string[::-1])



my_number = reverse_integer(-168)
print(my_number)