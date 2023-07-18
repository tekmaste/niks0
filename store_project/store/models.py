from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    info = models.TextField(blank=True)
    price = models.IntegerField()
    cats = models.ManyToManyField("Category", blank=True, related_name="products")
    image = models.ImageField(upload_to= "images/", default= 'images/default.jfif')

    def __str__(self):
        return self.title
    
    
class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Order(models.Model):
    name = models.CharField(max_length=100)
    tel = models.CharField(max_length=15)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    def __str__(self):
        return self.name