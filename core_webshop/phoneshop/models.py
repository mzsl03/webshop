from django.db import models
from django.contrib.postgres.fields import ArrayField

class Products(models.Model):

    categories = (
        ("1", "Telefon"),
        ("2", "Tartozék")
    )
    
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    category = models.CharField(choices=categories, default='1')
    colors = ArrayField(
        models.CharField(max_length=50),
        blank=False,
        default=list
    )
    image_path = ArrayField(
        models.CharField(max_length=255),
        blank=True,
        default=list
    )
    available = ArrayField(
        models.IntegerField(),
        blank=True,
        default=list
    )
    prices=ArrayField(
        models.IntegerField(),
        blank=False,
        default=list
    )
