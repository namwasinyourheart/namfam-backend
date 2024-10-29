from django.db import models

# Create your models here.
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
    # content = models.TextField(blank=True, null=True)
    # demoLink = models.URLField(blank=True, null=True)  # Make demoLink optional
    # repoLink = models.URLField(blank=True, null=True)  # Make repoLink optional
    # thumbnail = models.URLField(blank=True, null=True)  # Make thumbnail optional
    # keyFeatures = models.TextField(blank=True, null=True)
    # technologies = models.TextField(blank=True, null=True)
    # images = models.JSONField(blank=True, null=True)  # Make images optional
    thumbnail = models.URLField(blank=True, null=True)
    visible = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    


class ProjectDetails(models.Model):
    project = models.OneToOneField(Project, on_delete=models.CASCADE, related_name='details')  # One-to-one relationship with Project

    project_goal = models.TextField(blank=True, null=True)          # Project's main goal or objective
    tech_stack = models.TextField(blank=True, null=True)            # Technologies used in the project (e.g., Python, Django, React)
    features = models.TextField(blank=True, null=True)              # Key features of the project
    results = models.TextField(blank=True, null=True)               # Results or outcomes of the project
    challenges = models.TextField(blank=True, null=True)            # Challenges encountered during the project
    lessons_learned = models.TextField(blank=True, null=True)       # Lessons learned from the project
    demo_video = models.URLField(blank=True, null=True)
    # thumbnail = models.URLField(blank=True, null=True)
    # images = models.JSONField(blank=True, null=True)
    images = models.TextField(blank=True, null=True)
    demo_link = models.URLField(blank=True, null=True)  # Make demoLink optional
    repo_link = models.URLField(blank=True, null=True)  # Make repoLink optional


    # additional_info = models.TextField(blank=True, null=True)
    # timeline = models.TextField(blank=True, null=True)
    # team_members = models.TextField(blank=True, null=True)
    # budget = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # Optional budget field
    # completion_status = models.CharField(max_length=100, blank=True, null=True)  # E.g., "In progress", "Completed", etc.
    # notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Details for {self.project.title}"