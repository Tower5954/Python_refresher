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

user = {"username": "jose", "access_level": "not admin"}


def secure_function(func):
    if user["access_level"] == "admin":
        return func


get_admin_password_1 = secure_function(get_admin_password_1)

print("# ---- #")
# print(get_admin_password_1())

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

"""
----------- The '@' syntax for decorators------------
"""


@make_secure
def get_admin_password_2():
    return "12,13,14,15"


print(get_admin_password_2())

# when using decorators in this way. the 'get_admin_password_2'
# will no longer be a named function. it will be the one in the decorator
# this could be a problem in some other libraries, also any documentation
# attached to that function will be lost
print(get_admin_password_2.__name__)

# to combat this...

import functools


def make_secure_1(func):
    @functools.wraps(func)
    def secure_func():
        if user["access_level"] == "admin":
            return func()

    return secure_func


@make_secure_1
def get_admin_password_3():
    return "12,13,14,15"


print(get_admin_password_3.__name__)