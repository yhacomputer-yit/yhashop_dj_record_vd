from django.shortcuts import render , redirect , get_object_or_404
from django.contrib import messages
from .models import Category

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
    categories = Category.objects.all().order_by("id")
    return render(request, "category/admin-categories.html" , { "categories": categories,})

def admin_category_form(request):
    if request.method == "POST": 
        name = request.POST.get("name") 
        if name: 
            Category.objects.create(name=name) 
            messages.success(request, "Category created successfully!") 
            return redirect("admin_categories") 
    return render(request, "category/admin-category-form.html")

def category_delete(request, id): 
    category = get_object_or_404(Category, id=id) 
    if request.method == "POST": 
        category.delete() 
        messages.success(request, "Category deleted successfully!") 
        return redirect("admin_categories") 
    return render(request, "category/admin-category-delete.html", {"categories": 
category})

def category_edit(request, id):
    category = get_object_or_404(Category, id=id)
    if request.method == "POST":
        name = request.POST.get("name")
        if name:
            category.name = name
            category.save()
            messages.success(request, "Category updated successfully!")
            return redirect("admin_categories")
    return render(request, "category/admin-category-edit.html", {"category": category})

def admin_balance(request):
    return render(request, "balance/admin-balance.html")