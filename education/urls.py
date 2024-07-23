from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('DirectionList/', views.DirectionListView.as_view({'get': 'list', 'post': 'create'}), name='direction-list'),
    path('DirectionDetail/<int:id>/', views.DirectionDetailView.as_view(), name='direction-detail'),
    path('WhoIsThisProgramForList/', views.WhoIsThisProgramForListView.as_view({'get': 'list', 'post': 'create'}), name='who-this-for-list'),
    path('DirectionFAQList/', views.DirectionFAQListView.as_view({'get': 'list', 'post': 'create'}), name='direction-faq-list'),
    path('AdmissionProcessList/', views.AdmissionProcessListView.as_view({'get': 'list', 'post': 'create'}), name='admission-process-list'),
    path('EducationTypeList/', views.EducationTypeListView.as_view({'get': 'list', 'post': 'create'}), name='education-type-list'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
