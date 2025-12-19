class Library:
    books = []
    def add_book(self, book):
        self.books.append(book)
    def show_books(self):
        print(self.books)

b = Library()
b.add_book("Hello")
b.show_books()