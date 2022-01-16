from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator, RegexValidator


class Book(models.Model):
    title = models.CharField(
        verbose_name="Tytuł",
        max_length=255,
        )

    authors = models.CharField(
        verbose_name="Autorzy",
        max_length=255,
        blank=True,
        )

    publishedDate = models.DateField(
        verbose_name="Data publikacji",
        blank=True,
        null=True,
        )

    isbn = models.CharField(
        verbose_name="ISBN",
        max_length=13,
        unique=True,
        blank=True,
        null=True,
        validators=[
            RegexValidator(
                r"^\d{10}(\d{3})?$",
                message="Wprowadź prawidłowy 10- lub 13-cyfrowy identyfikator."),
            ],
        )

    pageCount = models.IntegerField(
        verbose_name="Ilość stron",
        blank=True,
        null=True,
        validators=[
            MinValueValidator(0,
                message="Ilość stron nie można być mniejsza niż zero.")
            ],
        )

    thumbnail = models.URLField(
        verbose_name="Odnośnik do okładki",
        max_length=255,
        blank=True,
        )

    language = models.CharField(
        verbose_name="Język",
        max_length=255,
        blank=True,
        )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("book_list")


class Keyword(models.Model):
    keyword = models.CharField(
        verbose_name="Wpisz słowo kluczowe",
        max_length=100,
        null=True,
        )
