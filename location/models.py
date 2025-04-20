from django.db import models

class Location(models.Model):
    first_name = models.CharField("Prénom", max_length=100)
    name = models.CharField("Nom", max_length=100)
    email = models.EmailField("Email")
    location_start = models.DateTimeField("Début de location")
    location_end = models.DateTimeField("Fin de location")
    phone_number = models.CharField("Numéro de téléphone", max_length=15, blank=True, null=True)
    association = models.TextField("Association (ex: Carpe, CI, ...)", blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.first_name})"

class Material(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='materials/', blank=True, null=True)

    def __str__(self):
        return self.name

class LocationMaterial(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name="materials")
    material = models.ForeignKey(Material, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.material.name} for {self.location.name}"
