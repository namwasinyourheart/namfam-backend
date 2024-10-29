# aboutme/serializers.py

from rest_framework import serializers
from .models import ProfessionalExperience, Education, Certifications, Resume
# , TechnicalSkill, Education, Certification, AdditionalInformation


class ProfessionalExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfessionalExperience
        fields = '__all__'


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'


class CertificationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certifications #Certifications
        fields = '__all__'

class ResumeSerializer(serializers.ModelSerializer):
    education = EducationSerializer()  # Nested EducationSerializer
    professional_experience = ProfessionalExperienceSerializer(many=True)  # Nested ProfessionalExperienceSerializer for many-to-many
    certifications = CertificationsSerializer(many=True)  # Nested CertificationsSerializer for many-to-many

    class Meta:
        model = Resume
        fields = '__all__'

# class TechnicalSkillSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = TechnicalSkill
#         fields = '__all__'





# class AdditionalInformationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = AdditionalInformation
#         fields = '__all__'
