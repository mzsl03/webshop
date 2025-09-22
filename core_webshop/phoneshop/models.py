from django.db import models

class Products(models.Model):

    categories = (
        (1, "Telefon"),
        (2, "Tartozék")
    )
    
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    category = models.CharField(choices=categories, default=1)