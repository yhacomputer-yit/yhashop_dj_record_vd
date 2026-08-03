from django.db import models

# Create your models here.

#category model

class Category(models.Model): 
    name = models.CharField(max_length=100) 
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True) 
    def __str__(self): 
        return self.name 
    
#product model

class Product(models.Model):
    name = models.CharField(max_length=100) 
    description = models.TextField() 
    price = models.DecimalField(max_digits=10, decimal_places=2) 
    category = models.ForeignKey(Category, on_delete=models.CASCADE) 
    image = models.ImageField(upload_to='products/')
    is_active = models.BooleanField(default=True)
    def __str__(self): 
        return self.name
    
