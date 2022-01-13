from api import views
from django.urls import path

urlpatterns = [
    path('', views.BookApiView.as_view(), name='api'),
]
