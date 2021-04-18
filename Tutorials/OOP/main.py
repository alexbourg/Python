# Python Object-Oriented programming

'''
data and functions = attributes and methods ( a function associated with a class)

Class
Instance of class
Class variables
Instance variables ## this video
'''

class Employee:
    num_of_emps = 0
    raise_amount = 1.04
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@outlook.com'

        Employee.num_of_emps += 1

    def fullname (self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(float(self.pay) * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


import datetime
my_date = datetime.date(2016, 7, 10)
print(Employee.is_workday(my_date))

# print(Employee.num_of_emps)
emp1 = Employee('Alex', 'Bourg', 50000)
emp2 = Employee('Anne', 'Smith', 60000)

emp_str_1 = 'John-Doe-7000'
emp_str_2 = 'Steven-Smith-3000'
emp_str_3 = 'Jane-Doe-9000'

new_emp_1 = Employee.from_string(emp_str_1)

# print(emp1.pay)
# emp1.apply_raise()
# print(emp1.pay)

# print(emp1.__dict__)
# print(Employee.__dict__)
# Employee.set_raise_amt(1.06)

# emp1.raise_amount = 1.05
# print(Employee.raise_amount)
# print(emp1.raise_amount)
# print(emp2.raise_amount)

# print(Employee.num_of_emps)

print(new_emp_1.email)




