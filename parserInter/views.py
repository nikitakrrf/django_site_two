
from django.shortcuts import render

def show_about(request):
    return render(request, 'parserInter/about.html')

def show_cart(request):
    return render(request, 'parserInter/cart.html')

def show_contact(request):
    return render(request, 'parserInter/contact.html')

def show_index(request):
    return render(request, 'parserInter/index.html')

def show_orders(request):
    return render(request, 'parserInter/orders.html')

def show_personal(request):
    return render(request, 'parserInter/personal.html')

def show_product(request):
    return render(request, 'parserInter/product.html')

def show_products(request):
    return render(request, 'parserInter/products.html')

