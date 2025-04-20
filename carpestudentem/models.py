from django.db import models


class Content(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField()


class ContentImage(models.Model):
    name = models.CharField(max_length=255)
    content = models.ImageField(upload_to="content_images/")


class ContentButton(models.Model):
    name = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    link = models.CharField(max_length=255)


class ProjectsPresentation(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    icon = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class NavbarButtons(models.Model):
    name = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ["order"]