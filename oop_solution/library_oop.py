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


class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    def add_book(self, book):
        if self.books.get(book.id) == None:
            self.books[book.id] = book
            print("Book added to Library")
        else:
            print("Book already exists")

    def add_member(self, member):
        if self.members.get(member.id) == None:
            self.members[member.id] = member
            print("Member registered")
        else:
            print("Member already registered")

    def borrow_book(self, member_id, book_id):
        member = self.members.get(member_id)
        book = self.books.get(book_id)

        if not member:
            print("Member not found!")
            return
        if not book:
            print("Book not found!")
            return
        if not book.is_available():
            print("No copies available!")
            return

        book.borrow()
        member.borrow_book(book)

    def return_book(self, member_id, book_id):
        member = self.members.get(member_id)
        book = self.books.get(book_id)

        if not member or not book:
            print("Member or book not found!")
            return

        member.return_book(book_id)
        book.return_book()

    def display_available_books(self):
        print("\n--- Available Books ---")
        for book in self.books.values():
            if book.is_available():
                print(
                    f"{book.title} by {book.author} - {book.available_copies} copies available")

    def display_member_books(self, member_id):
        member = self.members.get(member_id)
        if not member:
            print("Member not found!")
            return
        member.display_borrowed_books()
