class Book:
    def __init__(self, title: str, author: str, num_pages: int,check_status: bool=True) -> None:
        self.title = title
        self.author = author
        self.num_pages = num_pages
        self.check_status = check_status
    def __str__(self) -> str:
        return f"Title: {self.title}, Author: {self.author}, Pages: {self.num_pages}, Check Status: {self.check_status}"
    
class Library:
    def __init__(self) -> None:
        self.books = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)

    def remove_book(self, book: Book) -> None:
        self.books.remove(book)

    def check_out_book(self, book: Book) -> None:
       found_book = self.search_book(book.title)
       if found_book:
            found_book.check_status = False
       else:
            print(f"Book '{book.title}' not found in the library.")
            print("Book not found in the library.")


    def check_in_book(self, book: Book) -> None:
        found_book = self.search_book(book.title)
        if found_book:
            found_book.check_status = True
        else:
            print(f"Book '{book.title}' not found in the library.")
            print("Book not found in the library.")

    def display_books(self) -> None:
        for book in self.books:
            print(book)

    def search_book(self, title: str) -> Book:
        for book in self.books:
            if book.title == title:
                return book
        return None
    
book_1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 180, False)
book_2 = Book("To Kill a Mockingbird", "Harper Lee", 281, False)
book_3 = Book("1984", "George Orwell", 328, False)
book_4 = Book("Pride and Prejudice", "Jane Austen", 432, False)

library = Library()
library.add_book(book_1)
library.add_book(book_2)
library.add_book(book_3)
library.add_book(book_4)

# library.display_books()
# library.check_in_book(book_1)
library.remove_book(book_1)
library.display_books()