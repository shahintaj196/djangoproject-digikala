from django.db import models

# Create your models here.
class category(models.Model):
    name = models.CharField(max_lenght = 20 )
    
    def __str__(self):
        return self.name
    
    
class customer(models.Model):
    name = models.CharField(max_lenght = 20 )
    
    def __str__(self):
        return self.name