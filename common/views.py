from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *
from .models import *

class PositionistView(viewsets.ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer


class DepartmentListView(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class AdvertisementListView(viewsets.ModelViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer


class StatisticSectionView(viewsets.ModelViewSet):
    queryset = StatisticSection.objects.all()
    serializer_class = StatisticSectionSerializer


class StatisticListView(viewsets.ModelViewSet):
    queryset = Statistic.objects.all()
    serializer_class = StatisticSerializer


class EmployeeListView(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class NormativeDocumentListView(viewsets.ModelViewSet):
    queryset = NormativeDocument.objects.all()
    serializer_class = NormativeDocumentSerializer


class PurposeListView(viewsets.ModelViewSet):
    queryset = Purpose.objects.all()
    serializer_class = PurposeSerializer


class SiteMenuListView(viewsets.ModelViewSet):
    queryset = SiteMenu.objects.all()
    serializer_class = SiteMenuSerializer


class WhyChooseUsListView(viewsets.ModelViewSet):
    queryset = WhyChooseUs.objects.all()
    serializer_class = WhyChooseUsSerializer


class MainSliderListView(viewsets.ModelViewSet):
    queryset = MainSlider.objects.all()
    serializer_class = MainSliderSerializer


class InternationalCooperationListView(viewsets.ModelViewSet):
    queryset = InternationalCooperation.objects.all()
    serializer_class = InternationalCooperationSerializer


class RegionView(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


class VacancyListView(viewsets.ModelViewSet):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer


class ContactUsListView(viewsets.ModelViewSet):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer


class InfoView(viewsets.ModelViewSet):
    queryset = Info.objects.all()
    serializer_class = InfoSerializer


class HeaderInfoView(viewsets.ModelViewSet):
    queryset = HeaderInfo.objects.all()
    serializer_class = HeaderInfoSerializer


class FooterInfoView(viewsets.ModelViewSet):
    queryset = FooterInfo.objects.all()
    serializer_class = FooterInfoSerializer


class CountryListView(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class RegionListView(viewsets.ModelViewSet):
    queryset = RegionList.objects.all()
    serializer_class = RegionListSerializer


class PartnerListView(viewsets.ModelViewSet):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer


class SearchListView(viewsets.ModelViewSet):
    queryset = Search.objects.all()
    serializer_class = SearchSerializer


class SearchSuggestionListView(viewsets.ModelViewSet):
    queryset = SearchSuggestion.objects.all()
    serializer_class = SearchSuggestionSerializer


class OurMissionListView(viewsets.ModelViewSet):
    queryset = OurMission.objects.all()
    serializer_class = OurMissionSerializer


class OurStoryList(viewsets.ModelViewSet):
    queryset = OurStory.objects.all()
    serializer_class = OurStorySerializer


class TopHeaderMenuList(viewsets.ModelViewSet):
    queryset = TopHeaderMenu.objects.all()
    serializer_class = TopHeaderMenuSerializer


class FAQList(viewsets.ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer


class FrontendTranslationsView(viewsets.ModelViewSet):
    queryset = FrontendTranslation.objects.all()
    serializer_class = FrontendTranslationSerializer


class CitizenshipListView(viewsets.ModelViewSet):
    queryset = CitizenshipList.objects.all()
    serializer_class = CitizenshipListSerializer


class VacancyDetailView(APIView):
    def get(self, request, id):
        try:
            vacancy = Vacancy.objects.get(pk=id)
        except Vacancy.DoesNotExist:
            return Response({"error": "topilmadi"}, status=status.HTTP_404_NOT_FOUND)

        return Response({"id": vacancy.id, 'title': vacancy.title, 'work_time': vacancy.work_time, 'region': vacancy.region, 'is_active': vacancy.is_active})


class InternationalCooperationDetailView(APIView):
    def get(self, request, id):
        try:
            internationalcooperation = InternationalCooperation.objects.get(pk=id)
        except InternationalCooperation.DoesNotExist:
            return Response({"error": "topilmadi"}, status=status.HTTP_404_NOT_FOUND)

        return Response({"id": internationalcooperation.id, 'title': internationalcooperation.title, 'logo': internationalcooperation.logo, 'subtitle': internationalcooperation.subtitle, 'order': internationalcooperation.order})


class DepartmentDetailView(APIView):
    def get(self, request, id):
        try:
            department = Department.objects.get(pk=id)
        except Department.DoesNotExist:
            return Response({"error": "topilmadi"}, status=status.HTTP_404_NOT_FOUND)

        return Response({"id": department.id, 'title': department.title, 'slug': department.slug})


class SiteMenuDetailView(APIView):
    def get(self, request, id):
        try:
            sitemenu = SiteMenu.objects.get(pk=id)
        except SiteMenu.DoesNotExist:
            return Response({"error": "topilmadi"}, status=status.HTTP_404_NOT_FOUND)

        return Response({"id": sitemenu.id, 'title': sitemenu.title, 'slug': sitemenu.slug, 'front_url': sitemenu.front_url, 'order': sitemenu.order, 'children': sitemenu.children})


class EmployeeDetailView(APIView):
    def get(self, request, id):
        try:
            employee = Employee.objects.get(pk=id)
        except Employee.DoesNotExist:
            return Response({"error": "topilmadi"}, status=status.HTTP_404_NOT_FOUND)

        return Response({"id": employee.id, 'fullname': employee.fullname, 'surname': employee.position, 'photo': employee.photo, 'email': employee.email, "phone_number": employee.phone_number, 'short_description': employee.short_description, 'is_leader': employee.is_leader, 'department': employee.department})


class StaticPageDetailView(APIView):
    def get(self, request, id):
        try:
            statistic = Statistic.objects.get(pk=id)
        except Statistic.DoesNotExist:
            return Response({"error": "topilmadi"}, status=status.HTTP_404_NOT_FOUND)

        return Response({"id": statistic.id, 'name': statistic.statistic_section, 'title': statistic.title, 'value': statistic.value})