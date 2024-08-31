from django.db import models

class Project(models.Model):
    id = models.SlugField(primary_key=True, unique=True, max_length=100)
    title = models.CharField(max_length=200)
    description = models.TextField()
    content = models.TextField()
    demoLink = models.URLField()
    repoLink = models.URLField()
    thumbnail = models.URLField()
    keyFeatures = models.JSONField()
    technologies = models.JSONField()
    images = models.JSONField()

    def __str__(self):
        return self.title
