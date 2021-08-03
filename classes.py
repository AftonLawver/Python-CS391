# Practice using classes in python

class House():
    def __init__(self, floors, material, cost):
        self.floors = floors
        self.material = material
        self.cost = cost

    def get_floors(self):
        return self.floors

    def set_floors(self, x:int):
        self.floors = x
'''
my_house = House(3, "Wood", 345000)
my_house.set_floors(5)

number_of_floors = str(my_house.get_floors())
print("My house has " + number_of_floors + " floors")
'''

# Classes allow us to logically group our data and functions
# Methods = Function associated with a class

class Employee:

    # When we create instances within a class, they receive the instance as the 
    # first argument automatically. By convention, this is self.
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def full_name(self):
        return '{} {}'.format(self.first, self.last)

emp_2 = Employee('Afton', 'Lawver', 50000)
print(emp_2.email)
print(emp_2.full_name())




