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
    description = models.CharField(max_length=500, def)
    
    
    def __str__(self):
        return self.name