from django.contrib import admin
from .models import EnrollmentStep, EnrollmentRequirement, StudentService, Link

# Register your models here.
admin.site.register([EnrollmentStep, EnrollmentRequirement, StudentService, Link])