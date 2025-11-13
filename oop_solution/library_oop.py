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
