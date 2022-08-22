class ClassTest:
    def instance_method(self):
        print(f"Called instance_method of {self}")


test = ClassTest()

test.instance_method()
ClassTest.instance_method(test)

print(" ------- ")


class ClassTest1:
    def instance_method(self):
        print(f"Called instance_method of {self}")

    @classmethod
    def class_method(cls):
        print(f"Called class_method of {cls}")


ClassTest1.class_method()

print(" -------")


class ClassTest2:
    def instance_method(self):
        print(f"Called instance_method of {self}")

    @classmethod
    def class_method(cls):
        print(f"Called class_method of {cls}")

    @staticmethod
    def static_method():
        print("Called static_method")


ClassTest2.static_method()
print(" -------")


class Book:
    TYPES = ("Hardcover", "Paperback")


print(Book.TYPES)

print(" -------")


class Book1:
    TYPES = ("Hardcover", "Paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight


book = Book1("Lolita", "Hardcover", 1500 )

print(book.name)
print(Book1.TYPES)

print(" -------")


class Book2:
    TYPES = ("Hardcover", "Paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"<Book {self.name}, {self.book_type}, weighing: {self.weight}g"


book2 = Book2("Species", "Hardcover", 1600 )

print(book2)

print(" -------")


class Book3:
    TYPES = ("Hardcover", "Paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"<Book {self.name}, {self.book_type}, weighing: {self.weight}g"

    @classmethod
    def hardcover(cls, name, page_weight):
        return Book3(name, Book3.TYPES[0], page_weight + 100)


book3 = Book3.hardcover("Sapiens", 1600 )
print(book3)

print(" -------")


class Book4:
    TYPES = ("Hardcover", "Paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"<Book {self.name}, {self.book_type}, weighing: {self.weight}g"

    @classmethod
    def hardcover(cls, name, page_weight):
        return Book3(name, Book4.TYPES[0], page_weight + 100)

    @classmethod
    def paperback(cls, name, page_weight):
        return cls(name, cls.TYPES[1], page_weight)


book4 = Book4.paperback("deux machina", 600 )

print(book4)
