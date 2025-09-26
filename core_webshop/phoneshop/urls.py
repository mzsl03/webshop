from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.index, name='home'),
    path('receipts/', views.receipts),
    path('receipts/delete/<int:receipt_id>/', views.receipts, name='delete_receipt'),
    path('', views.login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('product/<str:name>/', views.product_detail, name='product-name'),
    path('cart/', views.user_cart, name='user_cart'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/delete/<int:item_id>/', views.delete_cart_item, name='delete_cart_item'),
    path('register/', views.register, name='register_worker'),
]
