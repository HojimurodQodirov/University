from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *
from .models import *


class EnrollmentStepListView(viewsets.ModelViewSet):
    queryset = EnrollmentStep.objects.all()
    serializer_class = EnrollmentStepSerializer


class EnrollmentRequirementListView(viewsets.ModelViewSet):
    queryset = EnrollmentRequirement.objects.all()
    serializer_class = EnrollmentRequirementSerializer


class StudentServiceListView(viewsets.ModelViewSet):
    queryset = StudentService.objects.all()
    serializer_class = StudentService


class StudentServiceDetailView(APIView):
    def get(self, request, id):
        try:
            studentservice = StudentService.objects.get(pk=id)
        except StudentService.DoesNotExist:
            return Response({"error": "topilmadi"}, status=status.HTTP_404_NOT_FOUND)

        return Response({"id": studentservice.id, 'title': studentservice.title, 'subtitle': studentservice.subtitle, 'icon': studentservice.icon})


class LinkListView(viewsets.ModelViewSet):
    queryset = Link.objects.all()
    serializer_class = Link
