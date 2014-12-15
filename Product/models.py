from django.db import models

# Create your models here.
class Product(models.Model):
    upc_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    description = models.TextField(null=True, blank=True)
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.name
    