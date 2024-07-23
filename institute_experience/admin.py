from django.contrib import admin
from .models import StudentProject, StudentBlog, StudentStory, FAQBranch, ScientificWorkCategory, ScientificWork, CampusPicture, Branch

admin.site.register([StudentProject, StudentBlog, StudentStory, FAQBranch, ScientificWorkCategory, ScientificWork, CampusPicture, Branch])
