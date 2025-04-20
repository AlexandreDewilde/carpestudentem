from django.db import models

class Edition(models.Model):
    name = models.CharField(max_length=255)
    poster = models.ImageField(upload_to='posters/')
    event_date = models.DateField()
    location = models.CharField(max_length=255)
    description = models.TextField()
    year = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} ({self.year})"


class Sponsor(models.Model):
    name = models.CharField(max_length=255)
    edition = models.ForeignKey(Edition, on_delete=models.CASCADE, related_name="sponsors")
    logo = models.ImageField(upload_to='logos/')

    def __str__(self):
        return self.name
