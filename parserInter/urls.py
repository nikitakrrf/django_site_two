from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('',show_index,name='home'),
    path('about/',show_about,name='about'),
    path('cart/',show_cart, name='cart'),
    path('contact/',show_contact,name='contact'),
    path('orders/',show_orders, name='orders'),
    path('personal/',show_personal,name='personal'),
    path('product/',show_product, name='product'),
    path('products/',show_products, name='products'),
]