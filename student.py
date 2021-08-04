# Lead Programmer: Afton Lawver

'''
Create a Student class and initialize it with name and ID number. Make methods to:
1. Display - It should display all informations of the student.
2. setAge - It should assign age to student
3. setMarks - It should assign marks to the student.
'''

class Student():

    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number
        

    def display(self):
        print("Student name: {}".format(self.name))
        print("Student ID number: {}".format(self.id_number))
        print("Student age: {}".format(self.age))
        print("Number of marks: {}".format(self.marks))

    def set_age(self, age):
        self.age = age

    def set_marks(self, marks):
        self.marks = marks

afton = Student("Afton", 851463587)
afton.set_marks(3)
afton.set_age(26)
afton.display()


