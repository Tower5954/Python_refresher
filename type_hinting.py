# Type hinting gives us tips and explains what the function, expects and what it needs in the arguments for example

# -- first example without type hinting (which would receive an error if called) -- #
def list_avg(sequence):
    return sum(sequence) / len(sequence)

# example that would error: "TypeError: 'int' object is not iterable" if called
# list_avg(123)


# Using type hinting and imports (most common way):
from typing import List  # , Tuple, Set, etc...


def list_avg_v2(sequence: List) -> float:
    return sum(sequence) / len(sequence)


print(list_avg_v2([1, 2, 3]))

# 2nd example in a class


class Book:
    def __init__(self, name: str, page_count: int):
        self.name = name
        self.page_count = page_count

    def __str__(self) -> str:
        return f"Title: {self.name}"


class Bookshelf:
    def __init__(self, books: List[Book]):
        self.books = books

    def __str__(self) -> str:
        return f"Bookshelf with: {len(self.books)} books"

    def unpack(self, books):
        book_no = Bookshelf
        for book in book_no:
            print(book)


book_1 = Book("Lolita", 365)
book_2 = Book("Mr Fantastic", 300)

bookshelf = Bookshelf([book_2, book_1])

print(bookshelf)
print(book_1)
print("# ---- #")
print(bookshelf.unpack)