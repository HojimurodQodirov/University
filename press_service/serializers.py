from rest_framework import serializers
from .models import *


class PressCategorySerializers(serializers.ModelSerializer):
    class Meta:
        models = PressCategory
        fields = ['id', "title", 'slug']


class NewsSerializers(serializers.ModelSerializer):
    category = PressCategorySerializers()

    class Meta:
        models = News
        fields = ['id', 'title', 'subtitle', 'slug', 'cover_image', 'category', 'published_at']


class EventSerializers(serializers.ModelSerializer):
    category = PressCategorySerializers()

    class Meta:
        models = Event
        fields = ['id', 'title', 'subtitle', 'slug', 'cover_image', 'category', 'published_at', 'event_date', 'button_text']
