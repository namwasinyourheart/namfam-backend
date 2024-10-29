# aboutme/urls.py

from django.urls import path
from .views import about_info, resume_info

urlpatterns = [
    path('about/', about_info, name='about-me'),
    path('resume/', resume_info)
]
