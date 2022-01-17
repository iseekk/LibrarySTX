import pytest
from books.forms import BookForm
from books.models import Book
from datetime import datetime

pytestmark = pytest.mark.django_db

BOOK_DATA = [
    {"title": "Foo",
     "authors": "Jan Kowalski",
     "publishedDate": "1990-01-01",
     "isbn": "1234567890",
     "pageCount": 100,
     "thumbnail": "https://example.com/",
     "language": "PL"},
    {"title": "Bar",
     "authors": "Paweł Nowak",
     "publishedDate": "2005-06-15",
     "isbn": "1234567891011",
     "pageCount": 200,
     "thumbnail": "https://example.com/",
     "language": "EN"},
    {"title": "Foo-Bar",
     "authors": "Tomasz Wójcik",
     "publishedDate": "2010-09-30",
     "isbn": "7654321234567",
     "pageCount": 300,
     "thumbnail": "https://example.com/",
     "language": "DE"},
]

@pytest.fixture
def one_book_db():
    book = Book.objects.create(**BOOK_DATA[0])
    return book

@pytest.fixture
def many_books_db():
    for data in BOOK_DATA:
        book = Book.objects.create(**data)


def test_title_is_enough():
    form = BookForm(data={"title": "Foo"})
    assert form.is_valid() == True


def test_clean_isbn():
        form = BookForm(data={"title": "Foo", "isbn": ""})
        form.is_valid()
        assert form.cleaned_data["isbn"] == None


# def test_clean(one_book_db):
#     form = BookForm(data={"title": "Foo"})
#     form.is_valid()
#     assert form.cleaned_data == False
