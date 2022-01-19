import pytest
from books.forms import BookForm
from books.models import Book
from datetime import date


pytestmark = pytest.mark.django_db

BOOK_DATA = {
    "title": "Foo",
    "authors": "Jan Kowalski",
    "publishedDate": "1990-01-01",
    "isbn": "1234567890",
    "pageCount": 100,
    "thumbnail": "https://example.com/",
    "language": "PL"
}


def test_title_is_enough():
    form = BookForm(data={"title": "Foo"})
    assert form.is_valid() == True


def test_bookform_clean_isbn():
    form = BookForm(data={"title": "Foo", "isbn": ""})
    form.is_valid()
    assert form.cleaned_data["isbn"] == None


def test_bookform_clean_return_false():
    """clean() should raise Error if titles are equal and there is no ISBN"""
    book = Book.objects.create(**{"title": "Foo"})
    form = BookForm(data={"title": "Foo"})
    form.is_valid()
    assert form.is_valid() == False
    assert form.errors["__all__"][0] == "Taka pozycja już istnieje w bazie danych"


def test_bookform_widgets():
    form = BookForm(data=BOOK_DATA)
    form.is_valid()
    assert isinstance(form.cleaned_data["publishedDate"], date) == True
