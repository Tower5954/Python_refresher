def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor can not be 0.")

    return dividend / divisor


def calculate(*values, operator):
    return operator(*values)


result = calculate(20, 4, operator=divide)
print(result)


def search(sequence, expected, finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem

    raise RuntimeError(f"Could not find an element with {expected}.")


friends = [
    {"name": "Rolf Smith", "age": 24},
    {"name": "Adam Wool", "age": 30},
    {"name": "Ann Pun", "age": 27}
]


def get_friend_name(friend):
    return friend["name"]


print(search(friends, "Rolf Smith", get_friend_name))

# -- using a lambda function as the finder -- #

print(search(friends, "Ann Pun", lambda friend: friend["name"]))

# -- using a built in function -- #
from operator import itemgetter
print(search(friends, "Adam Wool", itemgetter("name")))
