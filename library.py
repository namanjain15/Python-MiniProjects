class Book:
    # Constructor
    def __init__(self, title, author):
        self.title = title              # Public
        self.author = author            # Public
        self.__is_issued = False        # Private-style

    # Getter using decorator
    @property
    def is_issued(self):
        return self.__is_issued

    # Method to issue a book
    def issue_book(self):
        if not self.__is_issued:
            self.__is_issued = True
            print(f"'{self.title}' issued successfully!")
        else:
            print(f"'{self.title}' is already issued.")

    # Method to return a book
    def return_book(self):
        if self.__is_issued:
            self.__is_issued = False
            print(f"'{self.title}' returned successfully!")
        else:
            print(f"'{self.title}' was not issued.")

    # Display book details
    def display(self):
        status = "Issued" if self.is_issued else "Available"
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Status: {status}")



# Library class
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"'{book.title}' added to the library.")

    def show_books(self):
        if not self.books:
            print("No books available.")
            return

        print("\n--- Library Books ---")
        for book in self.books:
            print()
            book.display()
            print("--------------------")


# Create library object
library = Library()

# Create book objects
book1 = Book("Python Basics", "John Smith")
book2 = Book("Learn OOP", "David Miller")
book3 = Book("Data Structures", "Alice Johnson")

# Add books
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Display all books
library.show_books()

# Issue and return books
print("\n--- Book Transactions ---")
book1.issue_book()
book1.issue_book()
book1.return_book()

# Display final status
print("\n--- Updated Book Details ---")
book1.display()