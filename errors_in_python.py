def divide(dividend, divisor):
    if divisor == 0:
        print("Divisor can not be 0")
        return

    return dividend / divisor


divide(15, 0)

# ---- why errors are useful ---- #

# grades = [78, 99, 85, 100]
grades = []  # will run unclear message
print("Welcome to the average grade program.")
average = divide(sum(grades), len(grades))

print(f"The average grade is equal to: {average}")

print("# ----------- #")
# ---- functions with errors for debugging ---- #


def division(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be zero")

    return dividend / divisor


# grades_1 = []
# print("Welcome to the average grade program.")
# average_1 = division(sum(grades_1), len(grades_1))
#
# print(f"The average grade is equal to: {average_1}")

print("# ----------- #")
grades_2 = []
print("Welcome to the average grade program.")
try:
    average_2 = division(sum(grades_2), len(grades_2))
    print(f"The average grade is equal to: {average_2}")
except ZeroDivisionError as e:
    print("There are no grades yet in your list.")

# ---- other error types ---- #

# TypeError -- wrong type
# ValueError -- unexpected error
# Runtime Error

print("# ----------- #")

grades_3 = []
print("Welcome to the average grade program.")
try:
    average_3 = division(sum(grades_3), len(grades_3))
except ZeroDivisionError as e:
    print("There are no grades yet in your list.")
else:
    print(f"The average grade is equal to: {average_3}")

print("# ----------- #")

grades_4 = []
print("Welcome to the average grade program.")
try:
    average_4 = division(sum(grades_4), len(grades_4))
except ZeroDivisionError as e:
    print("There are no grades yet in your list.")
else:
    print(f"The average grade is equal to: {average_4}")
finally:
    print("Merci")

print("# ----------- #")
students = [
    {"Name": "Bob", "Grades": [75, 90]},
    {"Name": "Rolf", "Grades": []},
    {"Name": "Jen", "Grades": [100, 90]}
]

try:
    for student in students:
        name = student["Name"]
        grades_5 = student["Grades"]
        average_5 = division(sum(grades_5), len(grades_5))
        print(f"{name} averaged {average_5}")
except ZeroDivisionError:
    print(f"[ERROR]: {name} has no grades!")
else:
    print("-- All students averages calculated")
finally:
    print("-- End of student average calculation")

