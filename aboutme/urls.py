# aboutme/urls.py

from django.urls import path
from .views import about_me

urlpatterns = [
    path('about/', about_me, name='about-me'),
]
