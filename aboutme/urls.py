# aboutme/urls.py

from django.urls import path
from .views import resume_info

urlpatterns = [
    # path('about/', about_info, name='about-me'),
    path('resume/', resume_info)
]
