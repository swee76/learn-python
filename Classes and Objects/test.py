from Student import Student

student1 = Student("Sunil", "Business", 3.1, False)
student2 = Student("Pam", "Art", 2.1, True)

print("Student1 Name: " + student1.name)

print("Student2 gpa: " + str(student2.gpa))

student3 = Student("Jam", "Science", 3.8, True)

# Object Functions
print(student1.on_honor_roll())
print(student3.on_honor_roll())
