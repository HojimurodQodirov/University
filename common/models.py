from django.db import models
from press_service.models import News, Event


class FrontendTranslation(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)


class Advertisement(models.Model):
    title = models.CharField(max_length=255)
    image = models.URLField()
    link = models.URLField()
    expiration_date = models.DateTimeField()


class StatisticSection(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)


class Statistic(models.Model):
    statistic_section = models.ForeignKey(StatisticSection, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    value = models.IntegerField()


class Employee(models.Model):
    full_name = models.CharField(max_length=255)
    position = models.ForeignKey('Position', on_delete=models.CASCADE)
    photo = models.URLField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=255)
    short_description = models.TextField()
    is_leader = models.BooleanField()
    department = models.ForeignKey('Department', on_delete=models.CASCADE)


class Position(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)


class Department(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    order = models.IntegerField()


class NormativeDocument(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    file = models.URLField()
    images = models.URLField()


class Purpose(models.Model):
    type = models.CharField(max_length=255)
    description = models.TextField()
    image = models.URLField()
    order = models.IntegerField()


class SiteMenu(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    front_url = models.URLField()
    order = models.IntegerField()
    children = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)


class WhyChooseUs(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    image = models.URLField()
    order = models.IntegerField()


class MainSlider(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    image = models.URLField()
    video = models.URLField()
    front_url = models.URLField()


class InternationalCooperation(models.Model):
    title = models.CharField(max_length=255)
    logo = models.URLField()
    subtitle = models.CharField(max_length=255)
    order = models.IntegerField()


class Vacancy(models.Model):
    title = models.CharField(max_length=255)
    work_time = models.CharField(max_length=255)
    region = models.ForeignKey('Region', on_delete=models.CASCADE)
    is_active = models.BooleanField()


class ContactUs(models.Model):
    type = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    email = models.EmailField()


class Info(models.Model):
    phone_number = models.CharField(max_length=255)
    email = models.EmailField()
    site_url = models.URLField()
    phone_number_icon = models.URLField()
    email_icon = models.URLField()
    site_icon = models.URLField()
    location = models.URLField()


class HeaderInfo(models.Model):
    instagram_url = models.URLField()
    youtube_url = models.URLField()
    telegram_url = models.URLField()
    instagram_icon = models.URLField()
    youtube_icon = models.URLField()
    telegram_icon = models.URLField()
    location = models.URLField()
    phone_number = models.CharField(max_length=255)


class FooterInfo(models.Model):
    instagram_url = models.URLField()
    youtube_url = models.URLField()
    telegram_url = models.URLField()
    instagram_icon = models.URLField()
    youtube_icon = models.URLField()
    telegram_icon = models.URLField()


class Region(models.Model):
    name = models.CharField(max_length=255)


class Country(models.Model):
    name = models.CharField(max_length=255)


class RegionList(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)


class Partner(models.Model):
    title = models.CharField(max_length=255)
    logo = models.URLField()
    url = models.URLField()
    order = models.IntegerField()


class Search(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    events = models.ForeignKey(Event, on_delete=models.CASCADE)
    programmes = models.CharField(max_length=255)


class SearchSuggestion(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    type = models.CharField(max_length=255)


class OurMission(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    image = models.URLField()
    order = models.IntegerField()


class OurStory(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    image = models.URLField()
    order = models.IntegerField()


class TopHeaderMenu(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    front_url = models.URLField()


class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()


class CitizenshipList(models.Model):
    title = models.CharField(max_length=255)