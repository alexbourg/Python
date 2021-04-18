from Student_Class import Student


student1 = Student("Alex", "CyberSecuirty", 3.5, True)
student2 = Student("Bonbon", "Strategy", 4, False)

print(student1.name, student1.major, student1.gpa, student1.is_on_internship)
# print(student2.is_on_internship)

print(student1.on_honor_roll())