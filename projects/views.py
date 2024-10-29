from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view


from .serializers import TextInputSerializer
from .serializers import ProjectSerializer, CategorySerializer, ProjectDetailsSerializer

# from .chatbot import *
from rest_framework import status

from .models import Project, ProjectDetails

@api_view(['GET'])
def project_list(request):
    # projects = Project.objects.all()
    projects = Project.objects.filter(visible=True)
    serializer = ProjectSerializer(projects, many=True)  # Use the serializer to serialize the projects
    # print("serializer.data",serializer.data)
    return Response(serializer.data)


from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Project, ProjectDetails
from .serializers import ProjectSerializer, ProjectDetailsSerializer


@api_view(['GET'])
def project_detail(request, id):
    try:
        # Get the project by its primary key (id)
        project = Project.objects.get(id=id)

        # Serialize the project
        project_serializer = ProjectSerializer(project)
        
        # Try to get the associated ProjectDetails if they exist
        try:
            project_details = ProjectDetails.objects.get(project=project)
            project_details_serializer = ProjectDetailsSerializer(project_details)
            # Combine both project and project details data into one response
            response_data = {
                **project_serializer.data,
                **project_details_serializer.data,
            }
            
            # response_data = {
            #     'project_details': {
            #         **project_serializer.data,
            #         **project_details_serializer.data,
            #     }
            # }
        except ProjectDetails.DoesNotExist:
            # If project details don't exist, just return the project data under the combined key
            response_data = {
                'project_details': {
                    **project_serializer.data,
                    'project_details': None,
                }
            }
        
        return Response(response_data)
    
    except Project.DoesNotExist:
        return Response({'error': 'Project not found'}, status=status.HTTP_404_NOT_FOUND)



# @api_view(['GET'])
# def project_detail(request, id):
#     try:
#         # Get the project by its primary key (id)
#         project = Project.objects.get(id=id)

#         # print("project:", project)
        
#         # Serialize the project
#         project_serializer = ProjectSerializer(project)
        
#         # Try to get the associated ProjectDetails if they exist
#         try:
#             project_details = ProjectDetails.objects.get(project=project)
#             project_details_serializer = ProjectDetailsSerializer(project_details)
#             # Combine both project and project details data into one response
#             response_data = {
#                 'project': project_serializer.data,
#                 'project_details': project_details_serializer.data,
#             }
#         except ProjectDetails.DoesNotExist:
#             # If project details don't exist, just return the project data
#             response_data = {
#                 'project': project_serializer.data,
#                 'project_details': None,
#             }
        
#         return Response(response_data)
    
#     except Project.DoesNotExist:
#         return Response({'error': 'Project not found'}, status=status.HTTP_404_NOT_FOUND)


# @api_view(['GET'])
# def project_detail(request, id):
#     try:
#         project = Project.objects.get(pk=id)
#     except Project.DoesNotExist:
#         return Response({'error': 'Project not found'}, status=status.HTTP_404_NOT_FOUND)
    
#     serializer = ProjectSerializer(project)
#     # return Response(serializer.data)
#     return Response("Here is project data")
