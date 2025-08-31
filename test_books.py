import pytest
from books import Bookshelf


# -add books
def test_add_single_book_returns_true():
    shelf = Bookshelf()
    assert shelf.addBook("1984") is True

def test_add_duplicate_book_returns_false():
    shelf = Bookshelf()
    shelf.addBook("1984")
    assert shelf.addBook("1984") is False

def test_add_multiple_books_returns_true():
    shelf = Bookshelf()
    assert shelf.addBook("1984") is True
    assert shelf.addBook("Dune") is True
    assert shelf.addBook("Brave New World") is True

def test_add_books_list_contains_book():
    shelf = Bookshelf()
    shelf.addBook("1984")
    assert "1984" in shelf.getAllBooks()

def test_add_books_order_preserved():
    shelf = Bookshelf()
    shelf.addBook("1984")
    shelf.addBook("Dune")
    assert shelf.getAllBooks() == ["1984", "Dune"]

def test_add_empty_string_book():
    shelf = Bookshelf()
    assert shelf.addBook("") is True
    assert "" in shelf.getAllBooks()

def test_add_book_case_sensitive():
    shelf = Bookshelf()
    shelf.addBook("dune")
    assert shelf.addBook("Dune") is True


# --remove books
def test_remove_existing_book_returns_true():
    shelf = Bookshelf()
    shelf.addBook("1984")
    assert shelf.removeBook("1984") is True

def test_remove_nonexistent_book_returns_false():
    shelf = Bookshelf()
    assert shelf.removeBook("Dune") is False

def test_remove_book_really_removed():
    shelf = Bookshelf()
    shelf.addBook("1984")
    shelf.removeBook("1984")
    assert shelf.getAllBooks() == "no books on bookshelf"

def test_remove_book_from_multiple():
    shelf = Bookshelf()
    shelf.addBook("1984")
    shelf.addBook("Dune")
    shelf.removeBook("1984")
    assert shelf.getAllBooks() == ["Dune"]

def test_remove_book_twice_second_false():
    shelf = Bookshelf()
    shelf.addBook("1984")
    assert shelf.removeBook("1984") is True
    assert shelf.removeBook("1984") is False

def test_remove_empty_string_book():
    shelf = Bookshelf()
    shelf.addBook("")
    assert shelf.removeBook("") is True

def test_remove_preserves_others():
    shelf = Bookshelf()
    shelf.addBook("1984")
    shelf.addBook("Dune")
    shelf.removeBook("Dune")
    assert shelf.getAllBooks() == ["1984"]


# --get book
def test_get_existing_book_returns_name():
    shelf = Bookshelf()
    shelf.addBook("1984")
    assert shelf.getBook("1984") == "1984"

def test_get_nonexistent_book_returns_false():
    shelf = Bookshelf()
    assert shelf.getBook("Dune") is False

def test_get_book_after_remove_returns_false():
    shelf = Bookshelf()
    shelf.addBook("1984")
    shelf.removeBook("1984")
    assert shelf.getBook("1984") is False

def test_get_book_case_sensitive():
    shelf = Bookshelf()
    shelf.addBook("dune")
    assert shelf.getBook("Dune") is False

def test_get_book_from_multiple():
    shelf = Bookshelf()
    shelf.addBook("1984")
    shelf.addBook("Dune")
    assert shelf.getBook("Dune") == "Dune"

def test_get_empty_string_book():
    shelf = Bookshelf()
    shelf.addBook("")
    assert shelf.getBook("") == ""


# --get all book
def test_get_all_books_empty_returns_string():
    shelf = Bookshelf()
    assert shelf.getAllBooks() == "no books on bookshelf"

def test_get_all_books_single_book():
    shelf = Bookshelf()
    shelf.addBook("1984")
    assert shelf.getAllBooks() == ["1984"]

def test_get_all_books_multiple_books():
    shelf = Bookshelf()
    shelf.addBook("1984")
    shelf.addBook("Dune")
    assert shelf.getAllBooks() == ["1984", "Dune"]

def test_get_all_books_after_remove():
    shelf = Bookshelf()
    shelf.addBook("1984")
    shelf.addBook("Dune")
    shelf.removeBook("1984")
    assert shelf.getAllBooks() == ["Dune"]

def test_get_all_books_after_all_removed():
    shelf = Bookshelf()
    shelf.addBook("1984")
    shelf.removeBook("1984")
    assert shelf.getAllBooks() == "no books on bookshelf"

def test_get_all_books_order_is_correct():
    shelf = Bookshelf()
    shelf.addBook("A")
    shelf.addBook("B")
    shelf.addBook("C")
    assert shelf.getAllBooks() == ["A", "B", "C"]

def test_get_all_books_with_empty_string():
    shelf = Bookshelf()
    shelf.addBook("")
    shelf.addBook("1984")
    assert shelf.getAllBooks() == ["", "1984"]

def test_get_all_books_return_type_is_list():
    shelf = Bookshelf()
    shelf.addBook("1984")
    assert isinstance(shelf.getAllBooks(), list)

def test_get_all_books_return_type_is_string_if_empty():
    shelf = Bookshelf()
    assert isinstance(shelf.getAllBooks(), str)
