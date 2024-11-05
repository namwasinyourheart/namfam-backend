from django.shortcuts import render

# Create your views here.
# aboutme/views.py

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ProfessionalExperience, Certifications, Resume
# , TechnicalSkill, Education, Certification, AdditionalInformation
from .serializers import (
    SummarySerializer,
    ProfessionalExperienceSerializer,
    ResumeSerializer
    # , TechnicalSkillSerializer,
    # EducationSerializer, CertificationSerializer, AdditionalInformationSerializer
)

# @api_view(['GET'])
# def about_info(request):
#     experiences = ProfessionalExperience.objects.all()
#     # skills = TechnicalSkill.objects.all()
#     # education = Education.objects.all()
#     # certifications = Certifications.objects.all()
#     # additional_info = AdditionalInformation.objects.all()

#     data = {
#         'professional_experiences': ProfessionalExperienceSerializer(experiences, many=True).data,
#         # 'skills': TechnicalSkillSerializer(skills, many=True).data,
#         # 'education': EducationSerializer(education, many=True).data,
#         # 'certifications': CertificationSerializer(certifications, many=True).data,
#         # 'additional_info': AdditionalInformationSerializer(additional_info, many=True).data,
#     }
    
#     return Response(data)


# @api_view(['GET'])
# def resume_info(request):
#     resume = Resume.objects.all()

#     data = {
#         'resume': ResumeSerializer(resume, many=True).data,
#     }

#     print(data)

#     return Response(data)


@api_view(['GET'])
def resume_info(request):
    resumes = Resume.objects.prefetch_related('certifications', 'professional_experience', 'summary', 'others').select_related('education').all()
    print("resume:", resumes)
    serialized_resumes = ResumeSerializer(resumes, many=True)
    
    return Response({'resume': serialized_resumes.data})
