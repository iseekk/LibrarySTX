from books.models import Book
from books.filters import BookFilter
from books.forms import BookForm, KeywordForm
from books.funcs import download_book_data
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView
from django_filters.views import FilterView
from django.urls import reverse
from django.http import HttpResponseRedirect
from urllib.parse import quote_plus


class BookListView(FilterView):
    template_name = "books/book_list.html"
    filterset_class = BookFilter
    model = Book
    paginate_by = 10
    context_object_name = "books"
    ordering = ["-id"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        get_copy = self.request.GET.copy()
        if get_copy.get("page"):
            get_copy.pop("page")
        context["get_copy"] = get_copy
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
            idx = self.request.session["idx"]

            return reverse("book_repeat_search", kwargs={
                                                    "keyword": keyword,
                                                    "idx": idx,
                                                    })


def book_search(request, keyword=None, idx=0):

    if keyword:
        data, total_items = download_book_data(keyword, idx)
        request.session["keyword"] = keyword
        request.session["data"] = data
        request.session["total_items"] = total_items
        request.session["idx"] = idx
        return render(request, "books/book_results.html")

    elif request.method == "POST":

        if 'browse' in request.POST:
            form = KeywordForm(request.POST)

            if form.is_valid():
                keyword = quote_plus(form.cleaned_data["keyword"].strip().lower())
                data, total_items = download_book_data(keyword, idx)
                request.session["keyword"] = keyword
                request.session["data"] = data
                request.session["idx"] = idx
                request.session["total_items"] = total_items
                return render(request, "books/book_results.html")

        elif 'import_all' in request.POST:
            form = KeywordForm(request.POST)

            if form.is_valid():
                keyword = quote_plus(form.cleaned_data["keyword"].strip().lower())
                data, total_items = download_book_data(keyword, idx, max_results=40)
                curr_item = 0
                while total_items and curr_item < total_items:
                    for d in data:
                        d.pop("exists")
                        try:
                            book = Book.objects.create(**d)
                            book.save()
                        except Exception as e:
                            continue
                    data, total_items = download_book_data(keyword, idx, max_results=40)
                    idx += 40
                return HttpResponseRedirect(reverse("book_list"))

    else:
        form = KeywordForm()

    return render(request, "books/book_search.html", {"form": form})


def previous_page(request):
    keyword = request.session.pop("keyword")
    idx = request.session.pop("idx") - 10
    if idx < 10:
        idx = 0
    return HttpResponseRedirect(reverse("book_repeat_search", kwargs={
        "keyword": keyword,
        "idx": idx,
    }))


def next_page(request):
    keyword = request.session.pop("keyword")
    idx = request.session["idx"] + 10
    return HttpResponseRedirect(reverse("book_repeat_search", kwargs={
        "keyword": keyword,
        "idx": idx,
    }))
