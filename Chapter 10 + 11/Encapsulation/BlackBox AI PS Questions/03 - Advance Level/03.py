# Create a class Library that contains a list of Book objects. Each Book should have private attributes for title and author. Implement methods in Library to add and remove books, ensuring that the internal list of books is not directly accessible from outside the class.

class Book:
    def __init__(self):
        self.__title = ''
        self.__author = ''
        
    #taking title info
    @property
    def title(self):
        return f"Book Title: {self.__title}"

    @title.setter
    def title(self, title):
        self.__title = title
        
    
    #taking author info
    @property
    def author(self):
        return f"Book Author: {self.__author}"
    
    @author.setter
    def author(self, author):
        self.__author = author


class Library:
    def __init__(self):
        self.books = []

    #adding books to book list
    def add_book(self, book_title):
        self.books.append(book_title )
        
    #displaying books
    def display_books(self):
        return self.books



library = Library()

book = Book()
book.title = 'Shaheer Jamal Biography'
book.author = 'Shaheer Jamal'

book2 = Book()
book2.title = 'Altaf Hussain Biography'
book2.author = 'Altaf Hussain'


# print(book.title)
# print(book.author)

library.add_book(book.title)
library.add_book(book.author)

library.add_book(book2.title)
library.add_book(book2.author)

print(library.display_books())


