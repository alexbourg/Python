class Student:

    def __init__(self, name, major, gpa, is_on_internship):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_internship = is_on_internship

    def on_honor_roll(self):
        if self.gpa >= 3:
            return True
        else:
            return False
