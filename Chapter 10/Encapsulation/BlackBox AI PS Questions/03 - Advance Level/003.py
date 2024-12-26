class Book:
    def __init__(self):
        self.__title = ''
        self.__author = ''
        
    # Taking title info
    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        self.__title = title
        
    # Taking author info
    @property
    def author(self):
        return self.__author
    
    @author.setter
    def author(self, author):
        self.__author = author

class Library:
    def __init__(self):
        self._books = []

    # Adding books to the book list
    def add_book(self, book):
        if isinstance(book, Book):
            self._books.append(book)
            print(f'Book "{book.title}" by {book.author} added to the library.')
        else:
            print("Only Book objects can be added!")

    # Removing a book from the list
    def remove_book(self, specific_book_title, specific_book_author):
        for book in self._books:
            if book.title == specific_book_title and book.author == specific_book_author:
                self._books.remove(book)
                print(f'Book "{book.title}" by {book.author} removed from the library.')
                return
        print("Book not found in the library!")

    # Displaying books
    def display_books(self):
        if not self._books:
            print("The library has no books.")
        else:
            print("Books in the library:")
            for book in self._books:
                print(f' - "{book.title}" by {book.author}')

# Example Usage
# Creating a Library object
library = Library()

# Creating Book objects
book1 = Book()
book1.title = "1984"
book1.author = "George Orwell"

book2 = Book()
book2.title = "To Kill a Mockingbird"
book2.author = "Harper Lee"

# Adding books to the library
library.add_book(book1)
library.add_book(book2)

# Displaying books
library.display_books()

# Removing a book
library.remove_book("1984", "George Orwell")

# Displaying books after removal
library.display_books()
