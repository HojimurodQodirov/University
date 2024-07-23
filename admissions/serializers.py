from rest_framework import serializers
from .models import *


class EnrollmentStepSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnrollmentStep
        fields = ['title', 'body', 'icon']


class EnrollmentRequirementSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnrollmentRequirement
        fields = ['body']


class StudentServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentService
        fields = ['title', 'subtitle', 'icon']


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ['title', 'url', 'icon']

