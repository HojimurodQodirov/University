from django.contrib import admin
from .models import PressCategory, News, Event

# Register your models here.
admin.site.register([PressCategory, News, Event])