from django.contrib import admin
from .models import Products, Shops, Specs, Workers

admin.site.register(Products)
admin.site.register(Specs)
admin.site.register(Shops)
admin.site.register(Workers)