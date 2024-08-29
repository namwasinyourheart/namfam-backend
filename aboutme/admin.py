from django.contrib import admin

# Register your models here.
# aboutme/admin.py

from django.contrib import admin
from .models import ProfessionalExperience
# , TechnicalSkill, Education, Certification, AdditionalInformation

admin.site.register(ProfessionalExperience)
# admin.site.register(TechnicalSkill)
# admin.site.register(Education)
# admin.site.register(Certification)
# admin.site.register(AdditionalInformation)
