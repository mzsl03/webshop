import os
from sys import exception

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core_webshop.settings')
django.setup()
from phoneshop.models import Users


def Login(username, passwd):
    try:
        user = Users.objects.get(username=username)
        if passwd==user.password:
            return True
        else:
            return "password error"
    except Users.DoesNotExist:
        return "no user found"


def Register(worker, username, passwd):
    if Users.objects.filter(username=username).exists():
        return exception("user already exists")
    Users.objects.create(username=username, password=passwd)
    return "registration successful"