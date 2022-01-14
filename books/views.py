from books.models import Book
from books.filters import BookFilter
from books.forms import BookForm, KeywordForm
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView
from django_filters.views import FilterView
import urllib
import json
import re


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


def book_search(request):
    if request.method == "POST":
        form = KeywordForm(request.POST)
        if form.is_valid():
            keyword = urllib.parse.quote_plus(
                form.cleaned_data["keyword"].strip().lower()
            )
            url = f"https://www.googleapis.com/books/v1/volumes?q={keyword}"
            response = urllib.request.urlopen(url)
            data = json.loads(response.read())
            search_results = []
            for book in data["items"]:
                date = book["volumeInfo"]["publishedDate"] \
                    if "publishedDate" in book["volumeInfo"].keys() else ""
                if re.compile(r"^\d{4}\-(0[1-9]|1[012])$").match(date) is not None:
                    date = f"{date}-01"
                elif re.compile(r"^\d{4}$").match(date) is not None:
                    date = f"{date}-01-01"

                for i in book["volumeInfo"]["industryIdentifiers"]:
                    if "ISBN_13" in i.values():
                        isbn = i["identifier"]
                        break
                    elif "ISBN_10" in i.values():
                        isbn = i["identifier"]
                    else:
                        isbn = ""

                result = {
                    "title": book["volumeInfo"]["title"]
                    if "title" in book["volumeInfo"].keys() else "",

                    "authors": ", ".join(
                        [str(a) for a in book["volumeInfo"]["authors"]]
                    ) if "authors" in book["volumeInfo"].keys() else "",

                    "publishedDate": date,

                    "isbn": isbn,

                    "pageCount": str(book["volumeInfo"]["pageCount"])
                    if "pageCount" in book["volumeInfo"].keys() else "",

                    "thumbnail": book["volumeInfo"]["imageLinks"]["thumbnail"]
                    if "imageLinks" in book["volumeInfo"] else "",

                    "language": book["volumeInfo"]["language"].upper()
                    if "language" in book["volumeInfo"].keys() else "",
                }

                search_results.append(result)

            request.session["data"] = search_results
            form = BookForm
            return render(request, "books/book_results.html", {"form": form, "keyword": keyword})

    else:
        form = KeywordForm()

    return render(request, "books/book_search.html", {"form": form})
