from django.db import models

class Location(models.Model):
    first_name = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    location_start = models.DateTimeField()
    location_end = models.DateTimeField()
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    association = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.first_name})"

class Material(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class LocationMaterial(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name="materials")
    material = models.ForeignKey(Material, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.material.name} for {self.location.name}"
