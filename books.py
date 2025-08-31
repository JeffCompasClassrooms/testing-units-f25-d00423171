class Bookshelf:
    def __init__(self):
        self.books = []

    def addBook(self, book):
        if book in self.books:
            return False
        self.books.append(book)
        return True

    def removeBook(self, book):
        if book in self.books:
            self.books.remove(book)
            return True
        return False

    def getBook(self, book):
        if book in self.books:
            return book
        return False

    def getAllBooks(self):
        if not self.books:
            return "no books on bookshelf"
        return self.books
