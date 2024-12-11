# pixelpioneer/urls.py
from django.urls import path

from pixelpioneer.views import index


urlpatterns = [
    path('', index),
]