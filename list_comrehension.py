# map function

numbers = [1,2,3,4,5]

def square(x:int):
    xx = x*x
    return xx

numbers_squared = list(map(square,numbers))
print("Using the map function:") 
print(numbers_squared)
print()

# list comprehension
# can do the same thing in one line of code
squares = [i*i for i in numbers]
print("Using list comprehension: ")
print(squares)
print()


# Task: from a given list of names, create a new list that has only names 
# that start with A, B, and C.
names = ["Anna", "Ethan", "Mary", "Alliyah", "Nolan", "Afton", "Piotr","Buck", "Matt","Carol"]
names_modified = [i for i in names if i[0] == "A" or i[0] == "B" or i[0] == "C"]
print(names_modified)