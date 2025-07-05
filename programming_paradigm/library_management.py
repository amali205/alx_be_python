# 📗 Book class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # means the book is available

# 📘 Library class
class Library:
    def __init__(self):
        self._books = []  # empty list to store books

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and book._is_checked_out == False:
                book._is_checked_out = True
                print(f"{book.title} has been checked out.")
                return
        print("Sorry, book is not available.")

    def return_book(self, title):  # ✅ method name must match exactly
        for book in self._books:
            if book.title == title and book._is_checked_out:
                book._is_checked_out = False
                print(f"{book.title} has been returned.")
                return
        print("Book not found or was not checked out.")

    def list_available_books(self):
        print("Available books:")
        for book in self._books:
            if book._is_checked_out == False:
                print(f"{book.title} by {book.author}")
