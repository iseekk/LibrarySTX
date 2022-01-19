from api import views
from django.urls import path

urlpatterns = [
    path('books/', views.BooksApiView.as_view(), name='api'),
]
