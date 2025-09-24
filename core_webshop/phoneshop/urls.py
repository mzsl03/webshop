from django.contrib.auth import views as auth_views
from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.index, name='home'),
    path('cart/', views.cart),
    path('receipts/', views.receipts),
    path('', views.login, name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name = 'logout'),
    path('product/<str:name>/', views.product_detail, name='product-name'),
]