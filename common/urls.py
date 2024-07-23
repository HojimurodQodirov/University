from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('AdvertisementList/', views.AdvertisementListView.as_view({'get': 'list', 'post': 'create'}), name='advertisement-list'),
    path('FrontendTranslations/', views.FrontendTranslationsView.as_view({'get': 'list', 'post': 'create'}), name='frontend-translations'),
    path('Statistic/', views.StatisticListView.as_view({'get': 'list', 'post': 'create'}), name='statistic'),
    path('StaticPage/<int:id>/', views.StaticPageDetailView.as_view(), name='static-page-detail'),
    path('EmployeeList/', views.EmployeeListView.as_view({'get': 'list', 'post': 'create'}), name='employee-list'),
    path('EmployeeDetail/<int:id>/', views.EmployeeDetailView.as_view(), name='employee-detail'),
    path('NormativeDocumentList/', views.NormativeDocumentListView.as_view({'get': 'list', 'post': 'create'}), name='normative-document-list'),
    path('PurposeList/', views.PurposeListView.as_view({'get': 'list', 'post': 'create'}), name='purpose-list'),
    path('SiteMenuList/', views.SiteMenuListView.as_view({'get': 'list', 'post': 'create'}), name='site-menu-list'),
    path('SiteMenuDetail/<int:id>/', views.SiteMenuDetailView.as_view(), name='site-menu-detail'),
    path('DepartmentList/', views.DepartmentListView.as_view({'get': 'list', 'post': 'create'}), name='department-list'),
    path('DepartmentDetail/<int:id>/', views.DepartmentDetailView.as_view(), name='department-detail'),
    path('WhyChooseUsList/', views.WhyChooseUsListView.as_view({'get': 'list', 'post': 'create'}), name='why-choose-us-list'),
    path('MainSliderList/', views.MainSliderListView.as_view({'get': 'list', 'post': 'create'}), name='main-slider-list'),
    path('InternationalCooperationList/', views.InternationalCooperationListView.as_view({'get': 'list', 'post': 'create'}), name='international-cooperation-list'),
    path('InternationalCooperationDetail/<int:id>/', views.InternationalCooperationDetailView.as_view(), name='international-cooperation-detail'),
    path('VacancyList/', views.VacancyListView.as_view({'get': 'list', 'post': 'create'}), name='vacancy-list'),
    path('VacancyDetail/<int:id>/', views.VacancyDetailView.as_view(), name='vacancy-detail'),
    path('ContactUsList/', views.ContactUsListView.as_view({'get': 'list', 'post': 'create'}), name='contact-us-list'),
    path('Info/', views.InfoView.as_view({'get': 'list', 'post': 'create'}), name='info'),
    path('HeaderInfo/', views.HeaderInfoView.as_view({'get': 'list', 'post': 'create'}), name='header-info'),
    path('FooterInfo/', views.FooterInfoView.as_view({'get': 'list', 'post': 'create'}), name='footer-info'),
    path('CitizenshipList/', views.CitizenshipListView.as_view({'get': 'list', 'post': 'create'}), name='citizenship-list'),
    path('CountryList/', views.CountryListView.as_view({'get': 'list', 'post': 'create'}), name='country-list'),
    path('RegionList/', views.RegionListView.as_view({'get': 'list', 'post': 'create'}), name='region-list'),
    path('PartnerList/', views.PartnerListView.as_view({'get': 'list', 'post': 'create'}), name='partner-list'),
    path('SearchList/', views.SearchListView.as_view({'get': 'list', 'post': 'create'}), name='search-list'),
    path('SearchSuggestionList/', views.SearchSuggestionListView.as_view({'get': 'list', 'post': 'create'}), name='search-suggestion-list'),
    path('OurMissionList/', views.OurMissionListView.as_view({'get': 'list', 'post': 'create'}), name='our-mission-list'),
    path('OurStoryList/', views.OurStoryList.as_view({'get': 'list', 'post': 'create'}), name='our-story-list'),
    path('TopHeaderMenuList/', views.TopHeaderMenuList.as_view({'get': 'list', 'post': 'create'}), name='top-header-menu-list'),
    path('FAQList/', views.FAQList.as_view({'get': 'list', 'post': 'create'}), name='faq-list')
]

urlpatterns = format_suffix_patterns(urlpatterns)
