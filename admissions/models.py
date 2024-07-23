from django.db import models


class EnrollmentStep(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    icon = models.URLField()


class EnrollmentRequirement(models.Model):
    body = models.TextField()


class StudentService(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    icon = models.URLField()


class Link(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField()
    icon = models.URLField()

