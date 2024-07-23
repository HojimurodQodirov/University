from django.urls import path
from . import views

urlpatterns = [
    path('EnrollmentSteps/', views.EnrollmentStepListView.as_view({'get': 'list', 'post': 'create'}), name='enrollment-step-list'),
    path('EnrollmentRequirementList/', views.EnrollmentRequirementListView.as_view({'get': 'list', 'post': 'create'}), name='enrollment-requirement-list'),
    path('StudentServiceList/', views.StudentServiceListView.as_view({'get': 'list', 'post': 'create'}), name='student-service-list'),
    path('StudentServiceDetail/<int:id>/', views.StudentServiceDetailView.as_view(), name='student-service-detail'),
    path('LinkList/', views.LinkListView.as_view({'get': 'list', 'post': 'create'}), name='link-list'),
]
