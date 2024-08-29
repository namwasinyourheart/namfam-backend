from django.contrib import admin

# Register your models here.
# projects/admin.py

from django.contrib import admin
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'demoLink', 'repoLink')
    search_fields = ('title', 'description')
    list_filter = ('technologies',)
