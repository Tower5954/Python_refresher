def named(**kwargs):
    print(kwargs)


named(name="Bob", age=25)
named(name="Bob", age=25, job="Postman")


def name_age(name, age):
    print(name, age)


details = {"name": "Dave", "age": 32}

name_age(**details)

print()
print("print_nicely...")


def print_nicely(**kwargs):
    named(**kwargs)
    for arg, value in kwargs.items():
        print(f"{arg}: {value}")


print_nicely(name="Steve", age=17)


print()
print("Separating args and kwargs")


def both(*args, **kwargs):
    print(args)
    print(kwargs)


both(1, 2, 3, name="Lee", age=28)
