from django.shortcuts import render

# Create your views here.
# aboutme/views.py

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ProfessionalExperience
# , TechnicalSkill, Education, Certification, AdditionalInformation
from .serializers import (
    ProfessionalExperienceSerializer
    # , TechnicalSkillSerializer,
    # EducationSerializer, CertificationSerializer, AdditionalInformationSerializer
)

@api_view(['GET'])
def about_me(request):
    experiences = ProfessionalExperience.objects.all()
    # skills = TechnicalSkill.objects.all()
    # education = Education.objects.all()
    # certifications = Certification.objects.all()
    # additional_info = AdditionalInformation.objects.all()

    data = {
        'experiences': ProfessionalExperienceSerializer(experiences, many=True).data,
        # 'skills': TechnicalSkillSerializer(skills, many=True).data,
        # 'education': EducationSerializer(education, many=True).data,
        # 'certifications': CertificationSerializer(certifications, many=True).data,
        # 'additional_info': AdditionalInformationSerializer(additional_info, many=True).data,
    }
    
    return Response(data)
