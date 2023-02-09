from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('product', views.product_list, name='product'),
    path('search', views.product_search, name='search'),
    path('product-details/<slug>', views.product_details, name='product-details'),
    path('product-category/<slug>', views.product_category, name='product-category'),
    path('login', views.custom_login, name='login'),
    path('register', views.custom_register, name='register'),
    path('logout', views.custom_logout, name='logout'),
    path('users-dashboard', views.user_dashboard, name='user-dashboard'),

    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/', views.cart_detail, name='cart_detail'),

]
