from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *
from .models import *


class StudentProjectsListView(viewsets.ModelViewSet):
    queryset = StudentProject.objects.all()
    serializer_class = StudentProjectSerializer


class StudentProjectsDetailView(APIView):
    def get(self, request, id):
        try:
            studentproject = StudentProject.objects.get(pk=id)
        except StudentProject.DoesNotExist:
            return Response({"error": "topilmadi"}, status=status.HTTP_404_NOT_FOUND)

        return Response(
            {"id": studentproject.id, 'title': studentproject.title, 'slug': studentproject.slug})


class StudentBlogsListView(viewsets.ModelViewSet):
    queryset = StudentBlog.objects.all()
    serializer_class = StudentBlogSerializer


class StudentBlogsDetailView(APIView):
    def get(self, request, id):
        try:
            studentblog = StudentBlog.objects.get(pk=id)
        except StudentBlog.DoesNotExist:
            return Response({"error": "topilmadi"}, status=status.HTTP_404_NOT_FOUND)

        return Response(
            {"id": studentblog.id, 'title': studentblog.title, 'slug': studentblog.slug})


class StudentStoryListView(viewsets.ModelViewSet):
    queryset = StudentStory.objects.all()
    serializer_class = StudentStorySerializer


class StudentStoryDetailView(APIView):
    def get(self, request, id):
        try:
            studentstory = StudentStory.objects.get(pk=id)
        except StudentStory.DoesNotExist:
            return Response({"error": "topilmadi"}, status=status.HTTP_404_NOT_FOUND)

        return Response(
            {"id": studentstory.id, 'title': studentstory.title, 'slug': studentstory.slug})


class FAQBranchListView(viewsets.ModelViewSet):
    queryset = FAQBranch.objects.all()
    serializer_class = FAQBranchSerializer


class ScientificWorkCategoryListView(viewsets.ModelViewSet):
    queryset = ScientificWorkCategory.objects.all()
    serializer_class = ScientificWorkCategorySerializer


class ScientificWorkListView(viewsets.ModelViewSet):
    queryset = ScientificWork.objects.all()
    serializer_class = ScientificWorkSerializer


class ScientificWorkDetailView(APIView):
    def get(self, request, id):
        try:
            scientificwork = ScientificWork.objects.get(pk=id)
        except ScientificWork.DoesNotExist:
            return Response({"error": "topilmadi"}, status=status.HTTP_404_NOT_FOUND)

        return Response(
            {'id': scientificwork.id, 'title': scientificwork.title, 'subtitle': scientificwork.subtitle, 'slug': scientificwork.slug, 'category': scientificwork.category, 'views_count': scientificwork.views_count, 'published_at': scientificwork.published_at, 'cover_image': scientificwork.cover_image})


class CampusPictureListView(viewsets.ModelViewSet):
    queryset = CampusPicture.objects.all()
    serializer_class = CampusPictureSerializers


class BranchListView(viewsets.ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializers


