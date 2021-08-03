# Enumerate in Python

# Task 1
# create a list or any object that supports iteration
my_list = ["Afton", "Alliyah", "Azula"]

# create the enum object of the list
enum_object = enumerate(my_list)

# create a list of the enumerated list and print it out
print(list(enum_object))

# Task 2
# create a list or any object that supports iteration
my_list = ["Afton", "Alliyah", "Azula"]

# printing the iterations directly
for ele in enumerate(my_list):
    print(ele)
print

for count, ele in enumerate(my_list,start = 100):
    print(count, ele)
print





