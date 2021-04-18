class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first.lower() + '.' + last.lower() + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)



emp_1 = Employee('Alex', 'BOURG', 50000)
emp_2 = Employee('Anne-Cecile', "GERARD", 60000)

# print(Employee.fullname(emp_1))
print(emp_1.fullname())
print(emp_1.email)
print(emp_1.pay, "\n")
print(emp_2.fullname())
print(emp_2.email)
print(emp_2.pay)
