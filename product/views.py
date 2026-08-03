from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "home/home.html")

def about(request):
    return render(request, "home/about.html")

def product_page(request):
    return render(request, "home/product.html")

def products(request):
    return render(request, "home/products.html")

def admin_products(request):
    return render(request, "product/admin-products.html")

def admin_product_form(request):
    return render(request, "product/admin-product-form.html")

def admin_categories(request):
    return render(request, "category/admin-categories.html")

def admin_category_form(request):
    return render(request, "category/admin-category-form.html")

def admin_balance(request):
    return render(request, "balance/admin-balance.html")