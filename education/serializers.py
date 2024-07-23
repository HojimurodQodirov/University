from rest_framework import serializers
from .models import *


class EducationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationType
        fields = ['id','title', 'slug', 'has_program', 'order']


class DirectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direction
        fields = ['id',
                  'title', 'slug', 'cover_image', 'education_type', 'tuition_fee', 'prices', 'period']


class WhoIsThisProgramForSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhoIsThisProgramFor
        fields = ['id', 'title', 'body', 'icon']


class DirectionFAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = DirectionFAQ
        fields = ['id', 'faq', 'order']


class AdmissionProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdmissionProcess
        fields = ['id', 'title', 'body']

