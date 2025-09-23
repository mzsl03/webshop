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

class Specs(models.Model):

    product = models.OneToOneField(
        Products,
        on_delete=models.CASCADE,
        related_name='specs'
    )

    CPU_speed = models.CharField(max_length=255)
    CPU_type = models.CharField(max_length=255)
    display_size = models.CharField(max_length=255)
    resolution = models.CharField(max_length=255)
    display_technology = models.CharField(max_length=255)
    max_refresh_rate = models.CharField(max_length=255)
    Spen = models.BooleanField(default=False)
    camera = models.CharField(max_length=255)
    memory = models.CharField(max_length=255)
    storage = models.CharField(max_length=255)
    os = models.CharField(max_length=255)
    charge = models.CharField(max_length=255)
    sensors = models.CharField(max_length=255)
    size = models.CharField(max_length=255)
    weight = models.CharField(max_length=255)
    battery = models.IntegerField()
    release_date = models.DateField()