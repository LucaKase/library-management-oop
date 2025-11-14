# Library Management System

This project is all about refactoring a procedural Library Management System into an Object-Oriented one.  
The goal is to use OOP principles such as encapsulation, modularity, and abstraction to create a clean, maintainable, and extendable design.  
The system allows adding and managing books and members, borrowing and returning books, and displaying library information.

## File Structure

- `library_procedural.py`: Original procedural version of the library system.
- `test_procedural.py`: Comprehensive test script for the procedural version.
- `library_oop.py`: Object-Oriented implementation including the `Book`, `Member`, and `Library` classes.
- `test_oop.py`: Test script for the OOP version including integration tests.

## Book Class

Located in `library_oop.py`, the `Book` class represents a single book in the library.

### Attributes

- `id`: Unique identifier of the book.
- `title`: Title of the book.
- `author`: Author of the book.
- `total_copies`: Total number of copies available in the library.
- `available_copies`: Number of copies currently available for borrowing.

### Methods

- `borrow()`: Decreases the available copies if a copy is available; otherwise prints an error message.
- `return_book()`: Increases the number of available copies.
- `is_available()`: Returns `True` if there is at least one available copy, otherwise `False`.

## Member Class

Located in `library_oop.py`, the `Member` class represents a registered library member.

### Attributes

- `id`: Unique member identifier.
- `name`: Full name of the member.
- `email`: Email address of the member.
- `borrowed_books_list`: List containing all `Book` objects currently borrowed by the member.

### Methods

- `borrow_book(book)`: Adds the given `Book` object to the borrowed list.
- `return_book(book_id)`: Removes a book from the borrowed list based on its ID.
- `display_borrowed_books()`: Displays all books currently borrowed by the member.

## Library Class

Located in `library_oop.py`, the `Library` class manages all members and books and coordinates borrowing and returning operations.

### Attributes

- `books`: Dictionary storing all books (`{book_id: Book}`).
- `members`: Dictionary storing all members (`{member_id: Member}`).

### Methods

- `add_book(book)`: Adds a new `Book` object to the library collection.
- `add_member(member)`: Adds a new `Member` object to the library.
- `borrow_book(member_id, book_id)`: Allows a member to borrow a book if it is available.
- `return_book(member_id, book_id)`: Allows a member to return a borrowed book.
- `display_available_books()`: Prints all books that still have available copies.
- `display_member_books(member_id)`: Prints all books borrowed by a specific member.

## Testing

Located in `test_oop.py`, the test suite covers all classes and their integration.

### Basic Operations

- Adding books and members.
- Borrowing and returning books.
- Displaying available books and borrowed books.

### Edge Cases

- Borrowing unavailable books.
- Returning books not borrowed.
- Borrowing/returning for non-existent members or books.

### Integration Test

A final test simulates a complete workflow, from adding data to borrowing and returning, verifying that all classes interact correctly.

## Running the Code

To run the full OOP test suite, execute `test_oop.py` inside the `oop_solution` directory:

```bash
python3 test_oop.py
```
