from django import forms
from books.models import Book, Keyword


class BookForm(forms.ModelForm):
    error_css_class = 'error-block'
    class Meta:
        model = Book
        fields = ("title", "authors", "publishedDate", "isbn", "pageCount",
                  "thumbnail", "language")

        widgets = {
            "publishedDate": forms.DateInput(attrs={"type": "date"}),
        }

    def clean_isbn(self):
        if self.cleaned_data["isbn"] == "":
            return None
        else:
            return self.cleaned_data['isbn']

    def clean(self):
        cleaned_data = super().clean()
        if not self.cleaned_data["isbn"] and Book.objects.filter(
            title=cleaned_data["title"],
            authors=cleaned_data["authors"],
            publishedDate=cleaned_data["publishedDate"],
            language=cleaned_data["language"],
            ):
            raise forms.ValidationError("Taka pozycja już istnieje w bazie danych")
        return cleaned_data


class KeywordForm(forms.ModelForm):
    class Meta:
        model = Keyword
        fields = ("keyword",)
