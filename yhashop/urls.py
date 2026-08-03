"""
URL configuration for yhashop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from product import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('product/', views.product_page, name='product'),
    path('products/', views.products, name='products'),
    path('admin-products/', views.admin_products, name='admin_products'),
    path('admin-product-form/', views.admin_product_form, name='admin_product_form'),
    path('admin-categories/', views.admin_categories, name='admin_categories'),
    path('admin-category-form/', views.admin_category_form, name='admin_category_form'),
    path('admin-balance/', views.admin_balance, name='admin_balance'),
]
