# aboutme/serializers.py

from rest_framework import serializers
from .models import ProfessionalExperience, Education, Certifications, Resume, Summary, Others
# , TechnicalSkill, Education, Certification, AdditionalInformation

class SummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Summary
        fields = ['summary_text']


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


class OthersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Others
        fields = ['details']  # Serialize the details field


class ResumeSerializer(serializers.ModelSerializer):
    # summary = SummarySerializer(many=True)  # Include summaries
    summary = serializers.SerializerMethodField()
    education = EducationSerializer()  # Nested EducationSerializer
    professional_experience = ProfessionalExperienceSerializer(many=True)  # Nested ProfessionalExperienceSerializer for many-to-many
    certifications = CertificationsSerializer(many=True)  # Nested CertificationsSerializer for many-to-many
    others = OthersSerializer()  # Include Others serializer

    class Meta:
        model = Resume
        fields = '__all__'

    def get_summary(self, obj):
        # Concatenate all summary texts into a single string, separating with new lines
        summary = "\n".join([s.summary_text for s in obj.summary.all()])
        # print("summary:",summary)
        return summary
    

# class TechnicalSkillSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = TechnicalSkill
#         fields = '__all__'





# class AdditionalInformationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = AdditionalInformation
#         fields = '__all__'
