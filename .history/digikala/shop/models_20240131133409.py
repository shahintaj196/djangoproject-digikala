from django.db import models

# Create your models here.
class category(models.Model):
    name = models.CharField(max_lenght = 20 )
    
    def __str__(self):
        return self.name
    
    
class customer(models.Model):
    first_name = models.CharField(max_lenght = 30 )
    lasst_name = models.CharField(max_lenght = 30 )
    phone = models.CharField(max_lenght = 20 )
    email = models.EmailField(max_lenght = 100 )
    password = models.CharField(max_lenght = 50 )
    
    def __str__(self):
        return f'{self.}{}'