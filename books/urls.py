from books import views
from django.urls import path, re_path

urlpatterns = [
    path("", views.BookListView.as_view(), name="book_list"),
    path("book/new/", views.CreateBookView.as_view(), name="book_new"),
    path("book/<int:pk>/edit/", views.UpdateBookView.as_view(),
         name="book_edit"),
    path("book/search/", views.book_search, name="book_search"),
    path("book/search?keyword=<keyword>/", views.book_search,
         name="book_repeat_search"),
    path("book/import/", views.ImportBookView.as_view(), name="book_import"),
]
