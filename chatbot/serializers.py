from rest_framework import serializers

class TextInputSerializer(serializers.Serializer):
    text = serializers.CharField()

from .models import Project, Category

# class ProjectSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Project
#         fields = '__all__'



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']

class ProjectSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)  # Ensure categories are serialized correctly

    class Meta:
        model = Project
        fields = '__all__'
        # fields = ['id', 'title', 'description', 'categories', 'repoLink', 'demoLink']  # Add other fields as necessary