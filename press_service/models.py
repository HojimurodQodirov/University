from django.db import models


class PressCategory(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)


class News(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    cover_image = models.URLField()
    category = models.ForeignKey(PressCategory, on_delete=models.CASCADE)
    published_at = models.DateField()


class Event(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    cover_image = models.URLField()
    category = models.ForeignKey(PressCategory, on_delete=models.CASCADE)
    published_at = models.DateField()
    event_date = models.DateField()
    button_text = models.CharField(max_length=255)

