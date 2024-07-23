from django.db import models


class StudentProject(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)


class StudentBlog(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)


class StudentStory(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)


class FAQBranch(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    employee = models.ForeignKey('common.Employee', on_delete=models.CASCADE)


class ScientificWorkCategory(models.Model):
    title = models.CharField(max_length=255)


class ScientificWork(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    category = models.ForeignKey(ScientificWorkCategory, on_delete=models.CASCADE)
    views_count = models.IntegerField()
    published_at = models.DateField()
    cover_image = models.URLField()


class CampusPicture(models.Model):
    image = models.URLField()
    order = models.IntegerField()


class Branch(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    video_url = models.URLField()
    cover_image = models.URLField()

