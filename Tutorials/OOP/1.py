# Python Object-Oriented programming

'''
data and functions = attributes and methods ( a function associated with a class)

Class
Instance of class
Class variables
Instance variables ## this video
'''


class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@outlook.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp1 = Employee('Alex', 'Bourg', '5000')
emp2 = Employee('Anne', 'Smith', 6000)



print(emp1.fullname())
print(emp1.email)
print('\n')
print(Employee.fullname(emp2))






