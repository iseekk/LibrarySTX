import pytest
from books.models import Book, Keyword
from django.urls import reverse


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


@pytest.fixture
def one_book_db():
    book = Book.objects.create(**BOOK_DATA)
    return book


def test_book_title(one_book_db):
    book = Book.objects.get(pk=1)
    label = book._meta.get_field("title").verbose_name
    assert book.title == "Foo"
    assert label == "Tytuł"


def test_book_authors(one_book_db):
    book = Book.objects.get(pk=1)
    label = book._meta.get_field("authors").verbose_name
    assert book.authors == "Jan Kowalski"
    assert label == "Autorzy"


def test_book_publishedDate(one_book_db):
    book = Book.objects.get(pk=1)
    label = book._meta.get_field("publishedDate").verbose_name
    assert book.publishedDate.isoformat() == "1990-01-01"
    assert label == "Data publikacji"


def test_book_isbn(one_book_db):
    book = Book.objects.get(pk=1)
    label = book._meta.get_field("isbn").verbose_name
    assert book.isbn == "1234567890"
    assert label == "ISBN"


def test_book_pageCount(one_book_db):
    book = Book.objects.get(pk=1)
    label = book._meta.get_field("pageCount").verbose_name
    assert book.pageCount == 100
    assert label == "Ilość stron"


def test_book_thumbnail(one_book_db):
    book = Book.objects.get(pk=1)
    label = book._meta.get_field("thumbnail").verbose_name
    assert book.thumbnail == "https://example.com/"
    assert label == "Odnośnik do okładki"


def test_book_language(one_book_db):
    book = Book.objects.get(pk=1)
    label = book._meta.get_field("language").verbose_name
    assert book.language == "PL"
    assert label == "Język"


def test_book_get_absolute_url(one_book_db):
    book = Book.objects.get(pk=1)
    assert book.get_absolute_url() == reverse("book_list")


def test_keyword():
    keyword = Keyword.objects.create(keyword="Test")
    assert keyword.keyword == "Test"
    assert keyword._meta.get_field("keyword").verbose_name == "Wpisz słowo kluczowe"
