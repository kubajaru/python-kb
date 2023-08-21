from .book import Book

new_book: Book = Book("test", "Jakub", 360)

print(new_book.author)
print(new_book.get_title)