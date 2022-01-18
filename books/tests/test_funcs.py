import pytest
from books.funcs import download_book_data
from books import funcs


@pytest.fixture(scope="module")
def response(django_db_blocker):
    with django_db_blocker.unblock():
        return download_book_data("hobbit", 0)

def test_download_book_data_isinstance(response):
    assert isinstance(response[0], list) == True
    assert isinstance(response[1], int) == True


@pytest.mark.parametrize("field", ["title", "authors", "publishedDate", "isbn",
                                   "pageCount", "thumbnail", "language"])
def test_download_book_data_fields(response, field):
    assert (field in response[0][0]) == True
