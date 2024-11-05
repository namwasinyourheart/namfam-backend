from django.db import models

class Category(models.Model):
    name = models.TextField(unique=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    id = models.SlugField(primary_key=True, unique=True, max_length=100)
    title = models.CharField(max_length=200)
    description = models.TextField()
    categories = models.ManyToManyField(Category, default="Uncategorized")
    content = models.TextField(blank=True, null=True)
    demoLink = models.URLField(blank=True, null=True)  # Make demoLink optional
    repoLink = models.URLField(blank=True, null=True)  # Make repoLink optional
    thumbnail = models.URLField(blank=True, null=True)  # Make thumbnail optional
    keyFeatures = models.TextField(blank=True, null=True)
    technologies = models.TextField(blank=True, null=True)
    images = models.JSONField(blank=True, null=True)  # Make images optional
    visible = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class ProjectDescription(models.Model):
    id = models.SlugField(primary_key=True, unique=True, max_length=100)
    title = models.CharField(max_length=200)
    introduction = ""


# ---Sammple Project Details
# # Project Overview

# This is a **sample project** that demonstrates how to render Markdown in React.

# ## Features

# - Easy to use
# - Supports **bold** and *italic* text
# - Code blocks:

# \`\`\`javascript
# console.log("Hello, World!");
# \`\`\`

# ### Links

# Check the documentation [here](https://example.com).

# ### Task List

# - [x] Implement feature 1
# - [ ] Implement feature 2