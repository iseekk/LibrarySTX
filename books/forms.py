from django import forms
from books.models import Book, Keyword


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ("title", "authors", "publishedDate", "isbn", "pageCount",
                  "thumbnail", "language")

        widgets = {
            "publishedDate": forms.DateInput(attrs={"type": "date"}),
        }


class KeywordForm(forms.ModelForm):
    class Meta:
        model = Keyword
        fields = ("keyword",)
