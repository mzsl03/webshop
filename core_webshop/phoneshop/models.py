from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User


class Products(models.Model):
    categories = (
        ("telefon", "Telefon"),
        ("tartozek", "Tartozék")
    )

    name = models.CharField(max_length=255)
    price = models.IntegerField()
    category = models.CharField(choices=categories, default='telefon')
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
    prices = ArrayField(
        models.IntegerField(),
        blank=False,
        default=list
    )

    def __str__(self):
        return f"{self.name}"


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
    memory = ArrayField(
        models.CharField(max_length=255),
        blank=False,
        default=list
    )
    storage = ArrayField(
        models.CharField(max_length=255),
        blank=False,
        default=list
    )
    os = models.CharField(max_length=255)
    charge = models.CharField(max_length=255)
    sensors = models.CharField(max_length=255)
    size = models.CharField(max_length=255)
    weight = models.IntegerField()
    battery = models.IntegerField()
    release_date = models.DateField()

    def __str__(self):
        return f"{self.product.name} specifikációs adatai"


class Shops(models.Model):
    names = (
        ('westend', 'Westend'),
        ("árkád", 'Árkád'),
        ("pólus", "Pólus")
    )

    name = models.CharField(choices=names, default='westend')
    location = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"


class Workers(models.Model):
    positions = (
        ('uzletvezeto', 'Üzletvezető'),
        ('ertekesito', 'Értékesítő'),
        ('promoter', 'Promóter'),
    )

    last_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    birth_date = models.DateField()
    phone_number = models.CharField(max_length=12)
    position = models.CharField(choices=positions, default='uzletvezeto')
    shop = models.ForeignKey(
        Shops,
        on_delete=models.CASCADE,
        related_name='workers'
    )
    admin = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.last_name} {self.first_name}"


class Orders(models.Model):
    status_choices = (
        ("feldolgozás_alatt", "Feldolgozás alatt"),
        ("kiszállítva", "Kiszállítva"),
        ("törölve", "Törölve"),
    )

    product = models.ForeignKey(
        Products,
        on_delete=models.CASCADE,
        related_name='orders'
    )
    shop = models.ForeignKey(
        Shops,
        on_delete=models.CASCADE,
        related_name='orders'
    )
    quantity = models.IntegerField()
    order_time = models.DateTimeField()
    status = models.CharField(choices=status_choices, default="feldolgozás alatt")
    color = models.CharField(max_length=255)
    storage = models.IntegerField()

    def __str__(self):
        unit = "TB"
        if self.storage > 100:
            unit = "GB"
        return f"{self.product.name} rendelés {self.color} színnel {self.storage} {unit} tárhellyel"


class Users(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='phoneshop_user',
        null=False,
        blank=False
    )
    worker = models.ForeignKey(
        Workers,
        on_delete=models.CASCADE,
        related_name='users'
    )


class Storage(models.Model):
    product = models.ForeignKey(
        Products,
        on_delete=models.CASCADE,
        related_name='storage'
    )
    shop = models.ForeignKey(
        Shops,
        on_delete=models.CASCADE,
        related_name='storage'
    )
    quantity = models.IntegerField()
    num_items = ArrayField(
        models.IntegerField(),
        blank=False,
        default=list
    )

    def __str__(self):
        return f"{self.product.name} raktárkészlet {self.shop} üzletben"


class Sales(models.Model):
    product = models.ForeignKey(
        Products,
        on_delete=models.CASCADE,
        related_name='sales'
    )
    shop = models.ForeignKey(
        Shops,
        on_delete=models.CASCADE,
        related_name='sales'
    )
    user = models.ForeignKey(
        Users,
        on_delete=models.CASCADE,
        related_name='sales'
    )
    quantity = models.IntegerField()
    selling_time = models.DateTimeField()
    tax_number = models.CharField(max_length=10)
    zip_code = models.CharField(max_length=4)
    address = models.CharField(max_length=255)
    costumer_name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    price = models.IntegerField()
    color = models.CharField(max_length=255)
    storage = models.IntegerField()

    def __str__(self):
        return f"{self.costumer_name} vásárlása"


class Cart(models.Model):
    user = models.ForeignKey(
        Users,
        on_delete=models.CASCADE,
        related_name='cart'
    )
    product = models.ForeignKey(
        Products,
        on_delete=models.CASCADE,
        related_name='cart'
    )
    shop = models.ForeignKey(
        Shops,
        on_delete=models.CASCADE,
        related_name='cart'
    )
    quantity = models.IntegerField()
    price = models.IntegerField()
    color = models.CharField(max_length=255)
    storage = models.IntegerField()

    def __str__(self):
        return f"{self.user} felhasználónak kosárban levő termékei"
