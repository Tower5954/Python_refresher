class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


bob = Person("Bob", 35)
print(bob)


class PersonV1:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # print out a "nice" easy to read string for users
    def __str__(self):
        return f"Person: {self.name}, {self.age} years old"


bobv1 = PersonV1("Bob_1", 35)
print(bobv1)


class PersonV2:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # print out a "nice" easy to read string for users
    # def __str__(self):
    #     return f"Person: {self.name}, {self.age} years old"

    def __repr__(self):
        return f"<Person({self.name}, {self.age})>"


bobv2 = PersonV2("Bob_2", 35)
print(bobv2)
bobv2.__repr__()