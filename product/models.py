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
    
    
#balance model

class Balance(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='balances')
    income_qty = models.PositiveIntegerField(default=0)
    sales_qty = models.PositiveIntegerField(default=0)
    balance = models.PositiveIntegerField(default=0)
    date = models.DateField(auto_now_add=True)
    
    @classmethod
    def recalculate_balance(cls, product):
        running_balance = 0
        for balance_record in cls.objects.filter(product=product).order_by('id'):
            running_balance += balance_record.income_qty - balance_record.sales_qty
            balance_record.balance = running_balance
            balance_record.save(update_fields=['balance'])
        return running_balance
    
    def __str__(self):
        return  f"{self.product.name} - {self.balance}"
