from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *
from .models import *


class PressCategoryListView(viewsets.ModelViewSet):
    queryset = PressCategory.objects.all()
    serializer_class = PressCategorySerializers


class NewsListView(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializers


class NewsDetailView(APIView):
    def get(self, request, id):
        try:
            news = News.objects.get(pk=id)
        except News.DoesNotExist:
            return Response({"error": "topilmadi"}, status=status.HTTP_404_NOT_FOUND)

        return Response({"id": news.id, 'title': news.title, 'slug': news.slug, 'subtitle': news.subtitle, 'cover_image': news.cover_image, 'category': news.category, 'published_at': news.published_at})


class EventListView(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializers


class EventDetailView(APIView):
    def get(self, request, id):
        try:
            event = Event.objects.get(pk=id)
        except Event.DoesNotExist:
            return Response({"error": "topilmadi"}, status=status.HTTP_404_NOT_FOUND)

        return Response({"id": event.id, 'title': event.title, 'slug': event.slug, 'subtitle': event.subtitle, 'cover_image': event.cover_image, 'category': event.category, 'published_at': event.published_at, 'event_date': event.event_date, 'button_text': event.button_text})
