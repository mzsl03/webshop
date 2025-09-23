import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core_webshop.settings')
django.setup()

from support_files.sorting import sortName
from support_files.search import search_products
from support_files.login_register import Login, Register

#for product in sortName():
  #  print(f"{product.name}: {product.price} Ft")

for product in search_products("Samsung"):
    print(product.name)


#print(Login("feri123","5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8"))
#print(Register("feri123","1234"))