from django.urls import path
from . import views

# URL Config

urlpatterns = [
    path('', views.show_home, name='shop-home'),
    path('products/', views.show_products, name='shop-products'),
    path('customers/', views.show_customers, name='shop-customers')
]