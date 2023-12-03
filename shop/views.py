from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

pages = [
    {
        'title': 'home'
    },
    {
        'title': 'products'
    },

    {
        'title': 'customers'
    },

]

def show_home(request):
    context = {
        'pages': pages
    }
    return render(request, 'home.html', context)

def show_products(request):
    return render(request, 'products.html', { 'title': 'products' })

def show_customers(request):
    return render(request, 'customers.html', { 'title': 'customers' })