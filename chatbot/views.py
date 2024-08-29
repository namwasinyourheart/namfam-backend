from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import TextInputSerializer
from .serializers import ProjectSerializer

from .chatbot import *
from rest_framework import status

from .models import Project

@api_view(['GET'])
def project_list(request):
    projects = Project.objects.all().values()
    return Response(projects)

# @api_view(['GET'])
# def project_detail(request, project_id):
#     try:
#         project = Project.objects.get(id=project_id)
#         return Response(project)
#     except Project.DoesNotExist:
#         return Response({"error": "Project not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def project_detail(request, id):
    try:
        project = Project.objects.get(pk=id)
    except Project.DoesNotExist:
        return Response({'error': 'Project not found'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = ProjectSerializer(project)
    return Response(serializer.data)

# Create your views here.
@api_view(['POST'])
def chat(request):
    serializer = TextInputSerializer(data=request.data)

    if serializer.is_valid():
        text = serializer.validated_data['text']

        answer = get_answer(text)

        return Response(answer)
    
    return Response(serializer.errors, status=400)

from django.core.mail import send_mail
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['POST'])
def contact(request):
    name = request.data.get('name')
    email = request.data.get('email')
    message = request.data.get('message')

    if not all([name, email, message]):
        return Response({"error": "All fields are required."}, status=status.HTTP_400_BAD_REQUEST)

    try:
        send_mail(
            subject=f"Message from {name}",
            message=message,
            from_email=email,
            recipient_list=[settings.DEFAULT_FROM_EMAIL],
            fail_silently=False,
        )
        return Response({"success": "Message sent successfully."}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)