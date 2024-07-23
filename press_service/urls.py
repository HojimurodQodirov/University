from django.urls import path
from . import views

urlpatterns = [
    path('PressCategoryList/', views.PressCategoryListView.as_view({'get': 'list', 'post': 'create'}), name='press-category-list'),
    path('NewsList/', views.NewsListView.as_view({'get': 'list', 'post': 'create'}), name='news-list'),
    path('NewsDetail/<int:id>/', views.NewsDetailView.as_view(), name='news-detail'),
    path('EventList/', views.EventListView.as_view({'get': 'list', 'post': 'create'}), name='event-list'),
    path('EventDetail/<int:id>/', views.EventDetailView.as_view(), name='event-detail'),
]
