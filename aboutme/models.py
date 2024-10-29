from django.db import models

# Create your models here.
class Contact(models.Model):
    address = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    github = models.URLField()
    website = models.URLField()

class Education(models.Model):
    institution = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    duration = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.degree} at {self.institution}"


# class ProfessionalExperience(models.Model):
#     position = models.CharField(max_length=200)
#     company = models.CharField(max_length=200)
#     start_date = models.DateField()
#     end_date = models.DateField(null=True, blank=True)
#     description = models.TextField()

#     def __str__(self):
#         return f"{self.position} at {self.company}"
    

class ProfessionalExperience(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200, null=True)
    duration = models.CharField(max_length=100, null=True)
    responsibilities = models.TextField()

    def __str__(self):
        return f"{self.title} at {self.company}"
    

class TechnicalSkills(models.Model):
    category = models.TextField()
    skill = models.TextField()

    def __str__(self):
        return f"{self.skill} ({self.category})"
    

class Certifications(models.Model):
    title = models.TextField()
    issued_by = models.TextField()
    date = models.TextField(blank=True, null=True)
    link = models.URLField(max_length=500, blank=True, null=True)
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return f"{self.title} issued by {self.issued_by}"
    
class Resume(models.Model):
    professional_experience = models.ManyToManyField(ProfessionalExperience)
    education = models.OneToOneField(Education, on_delete=models.CASCADE)
    certifications = models.ManyToManyField(Certifications)

    def __str__(self):
        return f"Resume of Nam"


# class Education, Certifications, Others, Summary
