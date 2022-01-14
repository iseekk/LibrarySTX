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

    def clean_isbn(self):
        if self.cleaned_data['isbn'] == "":
            return None
        else:
            return self.cleaned_data['isbn']

    # def clean_publishedDate(self):
    #     if self.cleaned_data['publishedDate'] == "dd.mm.rrrr":
    #         return None
    #     else:
    #         return self.cleaned_data['publishedDate']


class KeywordForm(forms.ModelForm):
    class Meta:
        model = Keyword
        fields = ("keyword",)
