# -- This system will not work as anyone could get the admin password -- #

user = {"username": "jose", "access_level": "guest"}


def get_admin_password():
    return "1234"

print(get_admin_password())

# -- A simple way around this -- #
def get_admin_password_1():
    return "5678"


if user["access_level"] == "admin":
    print(get_admin_password_1())
else:
    print("[ACCESS DENIED]")

# However, the 'get_admin_password' is still unsecure as you can still print it off
print(get_admin_password_1())

# -- Next we could try defining a 'secure' function -- #

def secure_get_admin():
    if user["access_level"] == "admin":
        return "9101112"

print(secure_get_admin())
print(get_admin_password_1())

"""
However, this way means that you will have to add the if statement
to all functions if you want it to be secure. 
"""

# -- create a function that takes in a function -- #

user = {"username": "jose", "access_level": "admin"}


def secure_function(func):
    if user["access_level"] == "admin":
        return func


get_admin_password_1 = secure_function(get_admin_password_1)

print("# ---- #")
print(get_admin_password_1())

"""
This will only work when the user is already a 'admin', 
ideally we would like, to check if the user is an admin before the function is called. This is where we make a decorator
"""


def make_secure(func):
    def secure_func():
        if user["access_level"] == "admin":
            return func()

    return secure_func

get_admin_password_1 = make_secure(get_admin_password_1)

print("# ---- #")
print(get_admin_password_1())
