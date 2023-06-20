from django.db import models

class Product(models.Model):
    product_id = models.IntegerField()
    

class Location(models.Model):
    location_id = models.IntegerField()
    

class ProductMovement(models.Model):
    product_id = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    from_location = models.CharField(max_length=50)
    to_location = models.CharField(max_length=50)
    product = models.CharField(max_length=50)
    quantity = models.IntegerField()
