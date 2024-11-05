from django.contrib import admin

# Register your models here.
# aboutme/admin.py

from django.contrib import admin
from .models import ProfessionalExperience, Education, Certifications, Resume, Summary, Others
# , TechnicalSkill, Education, Certification, AdditionalInformation,

admin.site.register(ProfessionalExperience)
admin.site.register(Education)
admin.site.register(Summary)
admin.site.register(Resume)
admin.site.register(Certifications)
admin.site.register(Others)
# admin.site.register(TechnicalSkill)
# admin.site.register(Education)
# admin.site.register(AdditionalInformation)

from .models import TechnicalSkills
@admin.register(TechnicalSkills)
class TechnicalSkillAdmin(admin.ModelAdmin):
    list_display = ('skill', 'category')
    list_filter = ('category',)
    search_fields = ('skill',)
