from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=255)
    year = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} ({self.year})"

class Member(models.Model):
    team = models.ForeignKey(Team, related_name='members', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    nickname = models.CharField(max_length=255, blank=True, null=True)
    role = models.CharField(max_length=255)
    role_louvainpero = models.CharField(max_length=255, blank=True, null=True)
    picture = models.ImageField(upload_to='member_pictures/', blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.role})"