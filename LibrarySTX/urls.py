from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("api/", include("api.urls")),
    path("", include("books.urls")),
    path("admin/", admin.site.urls),
]
