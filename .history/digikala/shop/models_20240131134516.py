from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_lenght = 20 )
    
    def __str__(self):
        return self.name
    
    
class Customer(models.Model):
    first_name = models.CharField(max_lenght = 30 )
    lasst_name = models.CharField(max_lenght = 30 )
    phone = models.CharField(max_lenght = 20 )
    email = models.EmailField(max_lenght = 100 )
    password = models.CharField(max_lenght = 50 )
    
    def __str__(self):
        return f'{self.first_name}{self.lasst_name}'
    
    
    
    class Product(models.Model):
    name = models.CharField(max_lenght = 40 )
    description = models.CharField(max_leng)
    
    
    def __str__(self):
        return self.name