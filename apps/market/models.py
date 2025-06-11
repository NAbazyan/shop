from django.db import models

class Market(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='market_images/',
                              null=True, blank=True)
    slug = models.SlugField(unique=True, max_length=200)
    def __str__(self):
        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/',
                              null=True, blank=True)
    market = models.ForeignKey(Market, on_delete=models.CASCADE, related_name='products')
    
    def __str__(self):
        return self.name
    

