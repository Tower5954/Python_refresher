friend_ages = {"Gandolf": 125, "Sauron": 325, "Bilbo": 56}

print("Gandolf is: ", friend_ages["Gandolf"])

friend_ages["Legolas"] = 693

print(friend_ages)

friend_ages["Bilbo"] = 57
print(friend_ages)

friends = [
    {"name": "Logan", "age": 235},
    {"name": "Horus", "age": 450},
    {"name": "Fulgrim", "age": 238}
]

print(friends)
print(friends[1])
print(friends[1]["name"])

student_attendance = {"Rolf": 96, "Jim": 80, "Gary": 100}

for student in student_attendance:
    print(student)

for student in student_attendance:
    print(f"{student}: {student_attendance[student]}")

print("\n")
for student, attendance in student_attendance.items():
    print(f"{student}: {attendance}")

if "Bob" in student_attendance:
    print("Bob is in!")
else:
    print("Who is Bob?")

attendance_values = student_attendance.values()
print(sum(attendance_values) / len(attendance_values))