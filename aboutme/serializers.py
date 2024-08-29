# aboutme/serializers.py

from rest_framework import serializers
from .models import ProfessionalExperience
# , TechnicalSkill, Education, Certification, AdditionalInformation

class ProfessionalExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfessionalExperience
        fields = '__all__'

# class TechnicalSkillSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = TechnicalSkill
#         fields = '__all__'

# class EducationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Education
#         fields = '__all__'

# class CertificationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Certification
#         fields = '__all__'

# class AdditionalInformationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = AdditionalInformation
#         fields = '__all__'
