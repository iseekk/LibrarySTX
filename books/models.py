from django.db import models
from django.urls import reverse


class Book(models.Model):
    title = models.CharField(verbose_name="Tytuł", max_length=255)
    authors = models.CharField(verbose_name="Autorzy", max_length=255,
                               blank=True)
    publishedDate = models.DateField(verbose_name="Data publikacji", blank=True, null=True)
    isbn = models.CharField(verbose_name="ISBN", max_length=255, unique=True,
                            blank=True, null=True)
    pageCount = models.CharField(verbose_name="Ilość stron", max_length=255,
                                 blank=True)
    thumbnail = models.URLField(verbose_name="Odnośnik do okładki",
                                max_length=255, blank=True)
    language = models.CharField(verbose_name="Język", max_length=255, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("book_list")


class Keyword(models.Model):
    keyword = models.CharField(verbose_name="Wpisz słowo kluczowe",
                               max_length=100, null=True)
