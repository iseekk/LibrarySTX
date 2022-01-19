from books.models import Book
from rest_framework import serializers


class BooksSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = [
            'title', 'authors', 'publishedDate', 'isbn', 'pageCount',
            'thumbnail', 'language',
        ]
