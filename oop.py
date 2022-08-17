student = {"name": "Rolf", "grades": (89, 90, 93, 78, 90)}


def average(sequence):
    return sum(sequence) / len(sequence)


print(average(student["grades"]))

# -- ideally this is what you would want -- #
# print(student.average())

"""
Using Object-Oriented Programming
"""


class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average_grade(self):
        return sum(self.grades) / len(self.grades)


student = Student("Bob", (2, 46, 88, 1, 100))

print(student.name)
print(student.grades)
print(Student.average_grade(student))
print(student.average_grade())
