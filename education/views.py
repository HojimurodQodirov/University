from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *


class DirectionListView(viewsets.ModelViewSet):
    queryset = Direction.objects.all()
    serializer_class = DirectionSerializer


class DirectionDetailView(APIView):
    def get(self, request, id):
        try:
            direction = Direction.objects.get(pk=id)
        except Direction.DoesNotExist:
            return Response({"error": "topilmadi"}, status=status.HTTP_404_NOT_FOUND)

        return Response({"id": direction.id, 'title': direction.title, 'slug': direction.slug, 'cover_image': direction.cover_image, 'education_type': direction.education_type, 'tuition_fee': direction.tuition_fee, 'prices': direction.prices, 'period': direction.period})

# class DirectionExchangeProgramListView:
#     queryset = Direction.objects.all()
#     serializer_class = DirectionSerializer
#
#
# class DirectionExchangeProgramDetailView:
#     queryset = Direction.objects.all()
#     serializer_class = DirectionSerializer


class WhoIsThisProgramForListView(viewsets.ModelViewSet):
    queryset = WhoIsThisProgramFor.objects.all()
    serializer_class = WhoIsThisProgramForSerializer


class DirectionFAQListView(viewsets.ModelViewSet):
    queryset = DirectionFAQ.objects.all()
    serializer_class = DirectionFAQSerializer


class AdmissionProcessListView(viewsets.ModelViewSet):
    queryset = AdmissionProcess.objects.all()
    serializer_class = AdmissionProcessSerializer


class EducationTypeListView(viewsets.ModelViewSet):
    queryset = EducationType.objects.all()
    serializer_class = EducationTypeSerializer
