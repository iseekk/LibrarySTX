from books import views
from django.urls import path

urlpatterns = [
    path("", views.BookListView.as_view(), name="book_list"),
    path("book/new/", views.CreateBookView.as_view(), name="book_new"),
    path("book/<int:pk>/edit/", views.UpdateBookView.as_view(),
         name="book_edit"),
    path("book/search/", views.book_search, name="book_search"),
]
