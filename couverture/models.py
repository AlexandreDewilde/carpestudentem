from django.db import models

class CouvertureType(models.Model):
    name = models.CharField("Nom du type de couverture", max_length=50)

    def __str__(self):
        return self.name

class Couverture(models.Model):
    # Mandatory fields
    first_name = models.CharField("Prénom", max_length=100)
    name = models.CharField("Nom", max_length=100)
    email = models.EmailField("Email")
    organizer = models.CharField("Nom de l'organisateur", max_length=200)
    event_name = models.CharField("Nom de l'événement", max_length=200)
    place_name = models.CharField("Lieu", max_length=200)
    date = models.DateField("Date")
    duration_comments = models.TextField("Commentaires sur la durée")
    couverture_type = models.ForeignKey(
        CouvertureType,
        on_delete=models.CASCADE,
        verbose_name="Type de couverture"
    )

    # Optional fields
    phone_number = models.CharField("Numéro de téléphone", max_length=15, blank=True, null=True)
    specific_comments = models.TextField("Commentaires spécifiques", blank=True, null=True)

    def __str__(self):
        return f"{self.event_name} - {self.name}"
