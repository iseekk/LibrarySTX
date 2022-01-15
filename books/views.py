from books.models import Book
from books.filters import BookFilter
from books.forms import BookForm, KeywordForm
from books.funcs import download_book_data
from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView
from django_filters.views import FilterView
from django.urls import reverse
import urllib


class BookListView(FilterView):
    paginate_by = 30
    model = Book
    template_name = "books/book_list.html"
    ordering = ["-id"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filter"] = BookFilter(
            self.request.GET, queryset=self.get_queryset()
        )
        return context


class CreateBookView(CreateView):
    redirect_field_name = "books/book_list.html"
    form_class = BookForm
    model = Book


class UpdateBookView(UpdateView):
    redirect_field_name = "books/book_list.html"
    form_class = BookForm
    model = Book


class ImportBookView(CreateView):
    form_class = BookForm
    model = Book

    def get_success_url(self):
        if "keyword" in self.request.session:
            keyword = self.request.session.pop("keyword")
            return reverse("book_repeat_search", kwargs={"keyword": keyword})


def book_search(request, keyword=None):

    if keyword:
        data = download_book_data(keyword)
        request.session["keyword"] = keyword
        request.session["data"] = data
        return render(request, "books/book_results.html")

    elif request.method == "POST":
        form = KeywordForm(request.POST)
        if form.is_valid():
            keyword = urllib.parse.quote_plus(
                form.cleaned_data["keyword"].strip().lower()
            )
            data = download_book_data(keyword)
            request.session["keyword"] = keyword
            request.session["data"] = data
            return render(request, "books/book_results.html")

    else:
        form = KeywordForm()

    return render(request, "books/book_search.html", {"form": form})
