from api.models import CustomUser
from django.db import models


class Pet(models.Model):
    name = models.CharField(max_length=100)
    pet_sitter = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    owner = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="pets", blank=True, null=True
    )


class Booking(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
