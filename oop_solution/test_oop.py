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


def test_integration():
    print("-" * 30)
    print("LIBRARY MANAGEMENT SYSTEM - FULL INTEGRATION TEST")
    print("-" * 30)

    library = Library()

    print("\n--- TEST 1: Adding Books ---")
    library.add_book(Book(1, "Python Crash Course", "Eric Matthes", 3))
    library.add_book(Book(2, "Clean Code", "Robert Martin", 2))
    library.add_book(Book(3, "The Pragmatic Programmer", "Hunt & Thomas", 1))
    library.add_book(Book(4, "Design Patterns", "Gang of Four", 2))

    print("\n--- TEST 2: Registering Members ---")
    library.add_member(Member(101, "Alice Smith", "alice@email.com"))
    library.add_member(Member(102, "Bob Jones", "bob@email.com"))
    library.add_member(Member(103, "Carol White", "carol@email.com"))

    print("\n--- TEST 3: Display Available Books ---")
    library.display_available_books()

    print("\n--- TEST 4: Borrowing Books ---")
    library.borrow_book(101, 1)
    library.borrow_book(101, 2)
    library.borrow_book(102, 1)

    print("\n--- TEST 5: Display Member's Books ---")
    library.display_member_books(101)
    library.display_member_books(102)
    library.display_member_books(103)

    print("\n--- TEST 6: Borrowing Limit & Error Cases ---")
    library.borrow_book(101, 3)  # Third book OK
    library.borrow_book(999, 1)  # Nonexistent member
    library.borrow_book(101, 999)  # Nonexistent book

    print("\n--- TEST 7: Returning Books ---")
    library.return_book(101, 1)
    library.return_book(102, 1)
    library.return_book(103, 1)  # Invalid return

    print("\n--- TEST 8: Final Status ---")
    for member_id in library.members:
        library.display_member_books(member_id)
    library.display_available_books()

    print("\n" + "-" * 30)
    print("INTEGRATION TEST COMPLETE")
    print("-" * 30)


if __name__ == "__main__":
    print("=" * 60)
    print("LIBRARY MANAGEMENT SYSTEM -  OOP COMPREHENSIVE TEST")
    print("=" * 60, "\n")

    test_book_class()
    test_member_class()
    test_library_class()
    test_integration()
