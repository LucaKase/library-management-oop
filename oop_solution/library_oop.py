class Book:
    def __init__(self, id, title, author, total_copies):
        self.id = id
        self.title = title
        self.author = author
        self.total_copies = total_copies
        self.available_copies = total_copies  # because at the start its all copies

    def borrow(self):
        if self.is_available():
            self.available_copies -= 1
        else:
            print("No available copies")

    def return_book(self):
        self.available_copies += 1

    def is_available(self):
        return self.available_copies > 0


class Member:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email
        self.borrowed_books_list = []

    def borrow_book(self, book):
        self.borrowed_books_list.append(book)
        print(f"{self.name} borrowed {book.title}")

    def return_book(self, book_id):
        for book in self.borrowed_books_list:
            if book.id == book_id:
                self.borrowed_books_list.remove(book)
                print(f"{self.name} returned {book.title}")
                return
        print(f"{self.name} has not borrowed a book with ID {book_id}")

    def display_borrowed_books(self):
        print(f"\n--- Books borrowed by {self.name} ---")
        if not self.borrowed_books_list:
            print("No books currently borrowed")
        else:
            for book in self.borrowed_books_list:
                print(f"- {book.title} by {book.author}")
