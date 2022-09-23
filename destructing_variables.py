t = 5, 11

x, y = t

print(x)
print(y)
print(t)

student_attendance = {"Rolf": 96, "Jim": 80, "Gary": 100}

for student, attendance in student_attendance.items():
    print(f"{student}: {attendance}")

for t in student_attendance.items():
    print(t)

people = [("Bob", 42, "mechanic"), ("James", 24, "artist"), ("Harry", 32, "lecturer")]

for name, age, profession in people:
    print(f"Name: {name}, Age:{age}, Profession: {profession} ")
print("\n")
for person in people:
    print(f"Name: {person[0]}, Age:{person[1]}, Profession: {person[2]} ")


head, *tails = [1, 2, 3, 4, 5]

print(head)
print(tails)

*head, tail = [1, 2, 3, 4, 5]
print(head)
print(tail)