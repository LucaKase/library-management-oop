from library_oop import Book, Member, Library


def test_book_class():
    print("-" * 30)
    print("BOOK CLASS TESTS")
    print("-" * 30)

    print("\n--- TEST 1: Creating Books ---")
    book1 = Book(1, "1984", "George Orwell", 3)
    book2 = Book(2, "Clean Code", "Jeff", 2)

    print(f"Created: {book1.title} by {book1.author}")
    print(f"Available copies: {book1.available_copies}/{book1.total_copies}")

    print("\n--- TEST 2: Borrowing Books ---")
    book1.borrow()
    print(
        f"After borrowing: {book1.title} has {book1.available_copies} copies left")
    book1.borrow()
    book1.borrow()
    book1.borrow()  # This should print "No available copies"

    print("\n--- TEST 3: Returning Books ---")
    book1.return_book()
    print(
        f"After returning: {book1.title} has {book1.available_copies} copies available")

    print("\n--- TEST 4: Checking Availability ---")
    print(f"Is '{book1.title}' available? {book1.is_available()}")
    book1.borrow()
    book1.borrow()
    book1.borrow()
    print(
        f"Is '{book1.title}' available after all borrowed? {book1.is_available()}")

    print("\n" + "-" * 30)
    print("BOOK CLASS TEST COMPLETE")
    print("-" * 30)


def test_member_class():
    print("-" * 30)
    print("MEMBER CLASS TESTS")
    print("-" * 30)

    book1 = Book(1, "1984", "George Orwell", 3)
    book2 = Book(2, "Clean Code", "Jeff", 2)

    member = Member(101, "Alice Garden", "alice@email.com")

    member.borrow_book(book1)
    member.borrow_book(book2)

    member.display_borrowed_books()

    member.return_book(1)
    member.display_borrowed_books()

    member.return_book(3)

    print("\n" + "-" * 30)
    print("MEMBER CLASS TEST COMPLETE")
    print("-" * 30)


def test_library_class():
    print("-" * 30)
    print("LIBRARY CLASS TESTS")
    print("-" * 30)

    library = Library()

    book1 = Book(1, "1984", "George Orwell", 3)
    book2 = Book(2, "Clean Code", "Jeff", 2)
    library.add_book(book1)
    library.add_book(book2)

    member1 = Member(101, "Alice", "alice@email.com")
    member2 = Member(102, "Bob", "bob@email.com")
    library.add_member(member1)
    library.add_member(member2)

    library.borrow_book(101, 1)
    library.borrow_book(101, 2)
    library.borrow_book(102, 1)

    library.display_available_books()
    library.display_member_books(101)
    library.display_member_books(102)

    library.return_book(101, 1)
    library.display_available_books()

    print("\n" + "-" * 30)
    print("LIBRARY CLASS TEST COMPLETE")
    print("-" * 30)


if __name__ == "__main__":
    print("=" * 60)
    print("LIBRARY MANAGEMENT SYSTEM -  OOP COMPREHENSIVE TEST")
    print("=" * 60, "\n")

    test_book_class()
    test_member_class()
    test_library_class()
