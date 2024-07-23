from django.db import models


class EducationType(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    has_program = models.BooleanField()
    order = models.IntegerField()


class Direction(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    cover_image = models.URLField()
    education_type = models.ForeignKey(EducationType, on_delete=models.CASCADE)
    tuition_fee = models.IntegerField()
    prices = models.IntegerField()
    period = models.CharField(max_length=255)


class WhoIsThisProgramFor(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    icon = models.URLField()


class DirectionFAQ(models.Model):
    faq = models.ForeignKey('common.FAQ', on_delete=models.CASCADE)
    order = models.IntegerField()


class AdmissionProcess(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()

