from rest_framework import serializers

class TextInputSerializer(serializers.Serializer):
    text = serializers.CharField()

from .models import Project, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']


class ProjectSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)  # Ensure categories are serialized correctly

    class Meta:
        model = Project
        fields = '__all__'
        # fields = ['id', 'title', 'description', 'categories']
        # fields = ['id', 'title', 'description', 'categories', 'repoLink', 'demoLink']  

from .models import ProjectDetails
class ProjectDetailsSerializer(serializers.ModelSerializer):
    # If you want to display related project details, you can use nested serializers.
    # To include a nested project representation, you could uncomment this.
    # project = serializers.StringRelatedField()  # Or use ProjectSerializer if needed.

    class Meta:
        model = ProjectDetails
        fields = '__all__'
        # fields = [
        #     'project_id',        # You may replace 'project' with 'project_id' to show only the ID.
        #     'project_goal',
        #     'tech_stack',
        #     'features',
        #     'results',
        #     'challenges',
        #     'lessons_learned',
        #     'demo_video',
        # ]