# C:\PhotoMemories\photomemories\urls.py
from django.urls import path, include

urlpatterns = [
    path("", include("albums.urls")),
]