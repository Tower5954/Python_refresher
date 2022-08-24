class Bookshelf:
    def __init__(self, quantity):
        self.quantity = quantity

    def __str__(self):
        return f"Bookshelf with {self.quantity} books."


shelf = Bookshelf(300)

print(shelf)
print(" -------- ")
print("\n")

# Another class inheriting from the bookshelf class


class Book(Bookshelf):
    def __init__(self, name, quantity):
        super().__init__(quantity)
        self.name = name


book = Book("The Hobbit", 120)
print(book)
print(" -------- ")
print("\n")


# Add a __str__ method to make more sense to the book class
class Book1(Bookshelf):
    def __init__(self, name, quantity):
        super().__init__(quantity)
        self.name = name

    def __str__(self):
        return f"Book: {self.name}"


book1 = Book1("The Hobbit", 120)
print(book1)
print(" -------- ")
print("\n")


# Using composition

class Bookshelf1:
    def __init__(self, *books):
        self.books = books

    def __str__(self):
        return f"Bookshelf with {len(self.books)} books."


class Book2:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Book: {self.name}"


book3 = Book2("lotr")
book4 = Book2("Fellowship of the ring")
shelf1 = Bookshelf1(book3, book4)
print(shelf1)
print(book3)
print(shelf1.books)