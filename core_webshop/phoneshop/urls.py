from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.index, name='home'),
    path('receipts/', views.receipts, name='receipts'),
    path('receipts/delete/<int:id>/', views.delete_receipt, name='delete_receipt'),
    path('', views.login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('product/<str:name>/', views.product_detail, name='product-name'),
    path('cart/', views.user_cart, name='user_cart'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/delete/<int:item_id>/', views.delete_cart_item, name='delete_cart_item'),
    path('register/', views.register, name='register_worker'),
    path('add_prod/', views.add_product, name='add_product'),
    path('product/<int:product_id>/specs/edit/', views.edit_specs, name='edit_specs'),
    path('order/', views.list_orders, name="list_orders"),
    path("order/update/<int:order_id>/", views.update_order, name="update_order"),
    path('checkout/', views.checkout, name='checkout'),
    path('user_list/',views.user_list, name='user_list'),
    path('users/<int:user_id>/edit/', views.update_user, name='update_user'),
    path('export/report/', views.export_report_excel, name='export_report_excel'),

]
