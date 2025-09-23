from django.contrib import admin
from .models import Cart, Products, Sales, Shops, Specs, Storage, Workers, Orders, Users

admin.site.register(Products)
admin.site.register(Specs)
admin.site.register(Shops)
admin.site.register(Workers)
admin.site.register(Orders)
admin.site.register(Users)
admin.site.register(Storage)
admin.site.register(Sales)
admin.site.register(Cart)