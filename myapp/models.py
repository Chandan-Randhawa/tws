from django.db import models

# Create your models here.

class Products(models.Model):
    Title = models.CharField(max_length=100)
    Description = models.CharField(max_length=1024)
    Price = models.IntegerField()


class ProductDetail(models.Model):
    product = models.ForeignKey('Products', on_delete=models.CASCADE)
    date_fetched = models.DateField()
    
    
