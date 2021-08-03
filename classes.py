# Practice using classes in python
import math


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

    # Class variables: variables that are shared among all instances
    # of a class
    raise_amount = 1.04
    num_of_employees = 0

    # When we create instances within a class, they receive the instance as the 
    # first argument automatically. By convention, this is self.
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_employees += 1

    def full_name(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

#emp_2 = Employee('Afton', 'Lawver', 50000)
##emp_3 = Employee('Afton', 'Lawver', 50000)

#print(Employee.num_of_employees)

# Create a Vehicle class with max_speed and mileage instance attributes

class Vehicle():

    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

    

class Circle():

    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        # Area of a circle = pi * r*r
        print("Area of circle is: ")
        return (math.pi * self.radius**2)

    def get_circumference(self):
        print("Circumference of circle is: ")
        return (2 * math.pi * self.radius)


a = Circle(3)
print(a.get_area())
print(a.get_circumference())