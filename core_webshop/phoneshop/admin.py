from django.contrib import admin
from .models import Products, Shops, Specs

admin.site.register(Products)
admin.site.register(Specs)
admin.site.register(Shops)