from django.urls import path
from .views import chat, project_list, project_detail

urlpatterns = [
    path('chat/', chat, name="Chat"),
    path('projects/', project_list, name='project-list'),
    path('projects/<slug:id>/', project_detail, name='project-detail'),
]