from rest_framework import serializers
from .models import *


class StudentProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProject
        fields = ['id', 'title', 'slug']


class StudentBlogSerializer(serializers.ModelSerializer):
    class Meta:
        models = StudentBlog
        fields = ['id', 'title', 'slug']


class StudentStorySerializer(serializers.ModelSerializer):
    class Meta:
        models = StudentStory
        fields = ['id', 'title', 'slug']


class FAQBranchSerializer(serializers.ModelSerializer):
    class Meta:
        models = FAQBranch
        fields = ['id', 'question', 'answer', 'employee']


class ScientificWorkCategorySerializer(serializers.ModelSerializer):
    class Meta:
        models = ScientificWorkCategory
        fields = ['id', "title"]


class ScientificWorkSerializer(serializers.ModelSerializer):
    category = ScientificWorkCategory()

    class Meta:
        models = ScientificWork
        fields = ['id', 'title', 'subtitle', 'slug', 'category', 'views_count', 'published_at', 'cover_image']


class CampusPictureSerializers(serializers.ModelSerializer):
    class Meta:
        models = CampusPicture
        fields = ['id', 'image', 'order']


class BranchSerializers(serializers.ModelSerializer):
    class Meta:
        models = Branch
        fields = ['id', 'title', 'slug', 'subtitle', 'video_url', 'cover_image']
