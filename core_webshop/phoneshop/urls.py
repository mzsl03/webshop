from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.index, name='home'),
    path('cart/', views.cart),
    path('receipts/', views.receipts),
    path('', views.login, name = 'login'),
]