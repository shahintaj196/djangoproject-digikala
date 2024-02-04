from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 20 )
    
    def __str__(self):
        return self.name
    
    
class Customer(models.Model):
    first_name = models.CharField(max_length = 30 )
    last_name = models.CharField(max_length = 30 )
    phone = models.CharField(max_length = 20 )
    email = models.EmailField(max_length = 100 )
    password = models.CharField(max_length = 50 )
    
    def __str__(self):
        return f'{self.first_name}{self.last_name}'
    
    
    
    class Product(models.Model):
    name = models.CharField(max_length = 40 )
    description = models.CharField(max_length=500, default='',blank=True,null=True)
    price=models.DecimalField(default=0, max_digits=12, decimal_places=2)
    Category=models.ForeignKey(Category,on_delete=MOCASCADE)
    
    
    def __str__(self):
        return self.name