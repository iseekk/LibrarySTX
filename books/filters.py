from books.models import Book
from django.forms import DateInput
from django_filters import FilterSet, CharFilter, DateFilter


class BookFilter(FilterSet):
    title = CharFilter(
        field_name="title",
        label="Tytuł",
        lookup_expr="icontains",
    )
    authors = CharFilter(
        field_name="authors",
        label="Autorzy",
        lookup_expr="icontains",
    )
    language = CharFilter(
        field_name="language",
        label="Język",
        lookup_expr="icontains",
    )
    initial_date = DateFilter(
        field_name="publishedDate",
        label="Data publikacji od",
        lookup_expr="gte",
        widget=DateInput(attrs={"type": "date"}),
    )
    final_date = DateFilter(
        field_name="publishedDate",
        label="Data publikacji do",
        lookup_expr="lte",
        widget=DateInput(attrs={"type": "date"}),
    )

    class Meta:
        model = Book
        fields = ("title", "authors", "language", "initial_date", "final_date")
