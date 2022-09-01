class Book:
    def __init__(self, name: str, page_count: int):
        self.name = name
        self.page_count = page_count
        self.pages_read = 0

    def __repr__(self):
        return (
            f"<Book {self.name}, read {self.pages_read} pages out of {self.page_count}"
        )

    def read(self, pages: int):
        self.pages_read += pages
        print(f"You have now read {self.pages_read} pages out of {self.page_count}")


python101 = Book("Python 101", 50)
python101.read(35)
# -- This should not be able to happen, as we have stated that the book has only 50 pages -- #
python101.read(50)

# -- creating an error to stop this from happening -- #

class TooManyPagesReadError(ValueError):
    pass


class Book1:
    def __init__(self, name: str, page_count: int):
        self.name = name
        self.page_count = page_count
        self.pages_read = 0

    def __repr__(self):
        return (
            f"<Book {self.name}, read {self.pages_read} pages out of {self.page_count}"
        )

    def read(self, pages: int):
        if self.pages_read + pages > self.page_count:
            raise TooManyPagesReadError(
                f"You tried to read {self.pages_read + pages} pages, but this book only"
                f" has {self.page_count} pages "
                )
        self.pages_read += pages
        print(f"You have now read {self.pages_read} pages out of {self.page_count}")

python102 = Book1("Python 101", 50)
# python102.read(35)
# -- This should not be able to happen, as we have stated that the book has only 50 pages -- #
# python102.read(50)


# -- other way to get a better message -- #

try:
    python102.read(40)
    python102.read(19)
except TooManyPagesReadError as e:
    print(e)