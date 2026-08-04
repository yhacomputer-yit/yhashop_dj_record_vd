from django.shortcuts import render , redirect , get_object_or_404
from django.contrib import messages
from .models import Balance, Category, Product

# Create your views here.
def home(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, "home/home.html", {"products": products, "categories": categories})

def about(request):
    categories = Category.objects.all()
    return render(request, "home/about.html"  , {"categories": categories})

def product_page(request , product_id):
    categories = Category.objects.all()
    products = get_object_or_404(Product, id=product_id)
    current_balance = Balance.objects.filter(product=products).order_by('-id').first()
    return render(request, "home/product.html", {"categories": categories , "products": products, "current_balance": current_balance})

def products(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    category_id = request.GET.get("category")
    if category_id:
        products = products.filter(category_id=category_id)
        
    return render(request, "home/products.html" , {"categories": categories , "products": products})

def admin_products(request):
    products = Product.objects.all().order_by("id")
    return render(request, "product/admin-products.html", {"products": products})

def admin_product_form(request):
    categories = Category.objects.all()
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        price = request.POST.get("price")
        category_id = request.POST.get("category")
        image = request.FILES.get("image")
        is_active = request.POST.get("is_active") == "on"
        if name and description and price and category_id and image:
            category = get_object_or_404(Category, id=category_id)
            Product.objects.create(
                name=name,
                description=description,
                price=price,
                category=category,
                image=image,
                is_active=is_active
            )
            messages.success(request, "Product created successfully!")
            return redirect("admin_products")
    return render(request, "product/admin-product-form.html" , {"categories": categories})


def admin_product_edit(request, id):
    product = get_object_or_404(Product, id=id)
    categories = Category.objects.all()
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        price = request.POST.get("price")
        category_id = request.POST.get("category")
        image = request.FILES.get("image")
        is_active = request.POST.get("is_active") == "on"
        if name and description and price and category_id:
            category = get_object_or_404(Category, id=category_id)
            product.name = name
            product.description = description
            product.price = price
            product.category = category
            if image:
                product.image = image
            product.is_active = is_active
            product.save()
            messages.success(request, "Product updated successfully!")
            return redirect("admin_products")
    return render(request, "product/admin-product-edit.html", {"product": product, "categories": categories})

def admin_product_delete(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == "POST":
        product.delete()
        messages.success(request, "Product deleted successfully!")
        return redirect("admin_products")
    return render(request, "product/admin-product-delete.html", {"product": product})

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
    balance_records = Balance.objects.all().order_by("-id")
    products = Product.objects.all().order_by("id")
    if request.method == "POST":
        product_id = request.POST.get("product")
        income_qty = request.POST.get("income")
        sales_qty = request.POST.get("sale")
        
        if product_id and income_qty is not None and sales_qty is not None:
            product = get_object_or_404(Product, id=product_id)
            income_qty = int(income_qty)
            sales_qty = int(sales_qty)
            
            # Create a new Balance record
            balance_record = Balance.objects.create(
                product=product,
                income_qty=income_qty,
                sales_qty=sales_qty,
                balance=0  # Initial balance will be recalculated
            )
            
            # Recalculate the balance for the product
            Balance.recalculate_balance(product)
            
            messages.success(request, "Balance record added successfully!")
            return redirect("admin_balance")
    return render(request, "balance/admin-balance.html" , {"products": products , "balance_records": balance_records})


def admin_balance_delete(request, id):
    balance_record = get_object_or_404(Balance, id=id)
    if request.method == "POST":
        product = balance_record.product
        balance_record.delete()
        
        # Recalculate the balance for the product after deletion
        Balance.recalculate_balance(product)
        
        messages.success(request, "Balance record deleted successfully!")
        return redirect("admin_balance")
    return render(request, "balance/admin-balance-delete.html", {"balance_record": balance_record})

def admin_balance_edit(request, id):
    balance_record = get_object_or_404(Balance, id=id)
    products = Product.objects.all().order_by("id")
    
    if request.method == "POST":
        product_id = request.POST.get("product")
        income_qty = request.POST.get("income")
        sales_qty = request.POST.get("sale")
        
        if product_id and income_qty is not None and sales_qty is not None:
            product = get_object_or_404(Product, id=product_id)
            income_qty = int(income_qty)
            sales_qty = int(sales_qty)
            
            # Update the balance record
            balance_record.product = product
            balance_record.income_qty = income_qty
            balance_record.sales_qty = sales_qty
            balance_record.save()
            
            # Recalculate the balance for the product after update
            Balance.recalculate_balance(product)
            
            messages.success(request, "Balance record updated successfully!")
            return redirect("admin_balance")
    
    return render(request, "balance/admin-balance-edit.html", {"balance_record": balance_record, "products": products})