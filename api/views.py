from books.models import Book
from api.serializers import BooksSerializer
from rest_framework import generics


class BooksApiView(generics.ListCreateAPIView):
    serializer_class = BooksSerializer

    def get_queryset(self):
        queryset = Book.objects.all()

        title = self.request.query_params.get('title', None)
        authors = self.request.query_params.get('authors', None)
        language = self.request.query_params.get('language', None)
        initial_date = self.request.query_params.get('initial_date', None)
        final_date = self.request.query_params.get('final_date', None)

        if title is not None:
            queryset = queryset.filter(title__contains=title)
        if authors is not None:
            queryset = queryset.filter(authors__contains=authors)
        if language is not None:
            queryset = queryset.filter(language__contains=language)
        if initial_date is not None:
            queryset = queryset.filter(publishedDate__gte=initial_date)
        if final_date is not None:
            queryset = queryset.filter(publishedDate__lte=final_date)

        return queryset
