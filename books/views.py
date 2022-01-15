from books.models import Book
from books.filters import BookFilter
from books.forms import BookForm, KeywordForm
from books.funcs import download_book_data
from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView
from django_filters.views import FilterView
from django.urls import reverse
from django.http import HttpResponseRedirect
import urllib


class BookListView(FilterView):
    # paginate_by = 10 # NOT WORKING
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
            page = self.request.session["page"]
            return reverse("book_repeat_search", kwargs={
                "keyword": keyword,
                "page": page
            })


def book_search(request, keyword=None, page=0):

    if keyword:
        data, total_items  = download_book_data(keyword, page)
        request.session["keyword"] = keyword
        request.session["data"] = data
        request.session["total_items"] = total_items
        request.session["page"] = page
        return render(request, "books/book_results.html")

    elif request.method == "POST":
        form = KeywordForm(request.POST)
        if form.is_valid():
            keyword = urllib.parse.quote_plus(
                form.cleaned_data["keyword"].strip().lower()
            )
            data, total_items = download_book_data(keyword, page)
            request.session["keyword"] = keyword
            request.session["data"] = data
            request.session["page"] = page
            request.session["total_items"] = total_items
            return render(request, "books/book_results.html")

    else:
        form = KeywordForm()

    return render(request, "books/book_search.html", {"form": form})


def previous_page(request):
    keyword = request.session.pop("keyword")
    page = request.session["page"] - 10
    if page < 10:
        page = 0
    return HttpResponseRedirect(reverse("book_repeat_search", kwargs={
        "keyword": keyword,
        "page": page,
    }))

def next_page(request):
    keyword = request.session.pop("keyword")
    page = request.session["page"] + 10
    return HttpResponseRedirect(reverse("book_repeat_search", kwargs={
        "keyword": keyword,
        "page": page,
    }))
