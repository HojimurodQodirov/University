from rest_framework import serializers
from .models import *


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = ['title', 'slug']


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['title', 'slug', 'order']


class AdvertisementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = ['title', 'image', 'link', 'expiration_date']


class StatisticSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatisticSection
        fields = ['title', 'slug']


class StatisticSerializer(serializers.ModelSerializer):
    statistic_section = StatisticSectionSerializer()

    class Meta:
        model = Statistic
        fields = ['statistic_section', 'title', 'value']


class EmployeeSerializer(serializers.ModelSerializer):
    position = PositionSerializer()
    department = DepartmentSerializer()

    class Meta:
        model = Employee
        fields = ['id', 'full_name', 'position', 'photo', 'email', 'phone_number', 'short_description', 'is_leader', 'department']


class NormativeDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = NormativeDocument
        fields = ['id', 'title', 'slug', 'file', 'images']


class PurposeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purpose
        fields = ['id', 'type', 'description', 'image', 'order']


class SiteMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteMenu
        fields = ['id', 'title', 'slug', 'front_url', 'order', 'children']


class WhyChooseUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhyChooseUs
        fields = ['id', 'title', 'subtitle', 'image', 'order']


class MainSliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainSlider
        fields = ['id', 'title', 'subtitle', 'image', 'video', 'front_url']


class InternationalCooperationSerializer(serializers.ModelSerializer):
    class Meta:
        model = InternationalCooperation
        fields = ['id', 'title', 'logo', 'subtitle', 'order']


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['id', 'name']


class FrontendTranslationSerializer(serializers.ModelSerializer):
    class Meta:
        model = FrontendTranslation
        fields = ['id', 'title', 'subtitle']


class CitizenshipListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CitizenshipList
        fields = ['id', 'title']


class VacancySerializer(serializers.ModelSerializer):
    region = RegionSerializer()

    class Meta:
        model = Vacancy
        fields = ['title', 'work_time', 'region', 'is_active']


class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = ['id', 'type', 'address', 'phone_number', 'email']


class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = ['id', 'phone_number', 'email', 'site_url', 'phone_number_icon', 'email_icon', 'site_icon', 'location']


class HeaderInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeaderInfo
        fields = ["instagram_url", 'youtube_url', 'telegram_url', 'instagram_icon', 'youtube_icon', 'telegram_icon','location', 'phone_number']


class FooterInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FooterInfo
        fields = ['instagram_url', 'youtube_url', 'telegram_url', 'instagram_icon', 'youtube_icon', 'telegram_icon']


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['name']


class RegionListSerializer(serializers.ModelSerializer):
    country = CountrySerializer()

    class Meta:
        model = RegionList
        fields = ['country', 'name']


class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = ['id', 'title', 'logo', 'url', 'order']


class SearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Search
        fields = ['id', 'news', 'events', 'programmes']


class SearchSuggestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SearchSuggestion
        fields = ['id', 'title', 'slug', 'type']


class OurMissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurMission
        fields = ['id', 'title', 'subtitle', 'image', 'order']


class OurStorySerializer(serializers.ModelSerializer):
    class Meta:
        model = OurStory
        fields = ['id', 'title', 'subtitle', 'image', 'order']


class TopHeaderMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopHeaderMenu
        fields = ['id', 'title', 'slug', 'front_url']


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ['id', 'question', 'answer']
