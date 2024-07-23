from django.urls import path
from . import views

urlpatterns = [
    path('StudentProjectsList/', views.StudentProjectsListView.as_view({'get': 'list', 'post': 'create'}), name='student-projects-list'),
    path('StudentProjectsDetail/<int:id>/', views.StudentProjectsDetailView.as_view(), name='student-projects-detail'),
    path('StudentBlogsList/', views.StudentBlogsListView.as_view({'get': 'list', 'post': 'create'}), name='student-blogs-list'),
    path('StudentBlogsDetail/<int:id>/', views.StudentBlogsDetailView.as_view(), name='student-blogs-detail'),
    path('StudentStoryList/', views.StudentStoryListView.as_view({'get': 'list', 'post': 'create'}), name='student_story_list'),
    path('StudentStoryDetail/<int:id>/', views.StudentStoryDetailView.as_view(), name='student_story_detail'),
    path('FAQBranchList/', views.FAQBranchListView.as_view({'get': 'list', 'post': 'create'}), name='faq_branch_list'),
    path('ScientificWorkCategoryList/', views.ScientificWorkCategoryListView.as_view({'get': 'list', 'post': 'create'}), name='scientific-work-category-list'),
    path('ScientificWorkList/', views.ScientificWorkListView.as_view({'get': 'list', 'post': 'create'}), name='scientific-work-list'),
    path('ScientificWorkDetail/<int:id>/', views.ScientificWorkDetailView.as_view(), name='scientific-work-detail'),
    path('CampusPictureList/', views.CampusPictureListView.as_view({'get': 'list', 'post': 'create'}), name='campus_picture_list'),
    path('BranchList/', views.BranchListView.as_view({'get': 'list', 'post': 'create'}), name='branch-list'),
]
