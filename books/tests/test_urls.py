import pytest
from django.urls import reverse
from books.models import Book
from django.conf import settings as django_settings


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


@pytest.mark.parametrize("param", [
    "book_list",
    "book_new",
    "book_search",
    "book_import",
])
def test_render_no_kwargs_views(client, param):
    temp_url = reverse(param)
    response = client.get(temp_url)
    assert response.status_code == 200


def test_render_book_edit_view(client):
    Book.objects.create(**BOOK_DATA)
    temp_url = reverse("book_edit", kwargs={"pk": 1})
    response = client.get(temp_url)
    assert response.status_code == 200


def test_render_book_repeat_search_view(client):
    temp_url = reverse("book_repeat_search", kwargs={
        "keyword": "keyword",
        "idx": 1,
    })
    response = client.get(temp_url)
    assert response.status_code == 200


@pytest.mark.parametrize("param, curr_idx, target_idx", [
    ("previous_page", 10, 0),
    ("next_page", 0, 10),
])
def test_page_views(client, param, curr_idx, target_idx):
    temp_url = reverse(param)
    session = client.session
    session["keyword"] = "keyword"
    session["idx"] = curr_idx
    session.save()
    session_cookie_name = django_settings.SESSION_COOKIE_NAME
    client.cookies[session_cookie_name] = session.session_key
    response = client.get(temp_url)
    assert response.status_code == 302
    assert response.url == reverse("book_search")[:-1] + f"%3Fkeyword=keyword&i={target_idx}/"
