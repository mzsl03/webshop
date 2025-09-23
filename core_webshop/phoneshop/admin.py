from django.contrib import admin
from .models import Products, Shops, Specs, Workers, Orders, Users

admin.site.register(Products)
admin.site.register(Specs)
admin.site.register(Shops)
admin.site.register(Workers)
admin.site.register(Orders)
admin.site.register(Users)