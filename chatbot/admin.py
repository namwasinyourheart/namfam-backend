from django.contrib import admin

# Register your models here.
# projects/admin.py

from django.contrib import admin
from .models import Project, Category

# @admin.register(Project)
# class ProjectAdmin(admin.ModelAdmin):
#     list_display = ('title', 'description', 'categories', 'repoLink')
#     search_fields = ('title', 'description')
#     list_filter = ('technologies',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'get_categories', 'repoLink', 'visible')
    search_fields = ('title', 'description')
    list_filter = ('technologies',)

    def get_categories(self, obj):
        return ", ".join([category.name for category in obj.categories.all()])
    get_categories.short_description = 'Categories'  # Set a short description for the column header


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)