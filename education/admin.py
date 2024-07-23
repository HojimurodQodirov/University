from django.contrib import admin
from .models import EducationType, Direction, WhoIsThisProgramFor, DirectionFAQ, AdmissionProcess

# Register your models here.
admin.site.register([EducationType, Direction, WhoIsThisProgramFor, DirectionFAQ, AdmissionProcess])