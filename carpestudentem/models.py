from django.db import models


class Content(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField()


class ContentImage(models.Model):
    name = models.CharField(max_length=255)
    content = models.ImageField(upload_to="content_images/")


class ProjectsPresentation(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="projects_presentations/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
